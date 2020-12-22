# -*- coding: utf-8 -*-
import logging
from array import array
import os
from PIL import Image
import sys
import time
import re
import json

import azure.functions as func
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


eligible = ['171NVX75', 'DU748BH' ,'325J521', 'SK253CL', 'VZ0909MD', 'RI373KI']

subscription_key = "2c9af0bfaed84e52951e59ab40311380"
endpoint = "https://extractnumberplate.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# funkcja zwraca nagłówek - co rozpoznała na zdjęciu i dokładność 
def describe_image_plate(remote_image_url):
    description_results = computervision_client.describe_image(remote_image_url )
    return description_results.captions


# funkcja wykrywa obiekty, zwraca bounding-box
def detect_image_plate(remote_image_url):
    remote_image_url_objects = remote_image_url
    detect_objects_results_remote = computervision_client.detect_objects(remote_image_url_objects)
    return detect_objects_results_remote.objects


#Funkcja zwraca text z zdjęcia oraz lokalizację 
def detect_text_image(remote_image_url):
    remote_image_handw_text_url = remote_image_url
    recognize_handw_results = computervision_client.read(remote_image_handw_text_url,  raw=True)
    operation_location_remote = recognize_handw_results.headers["Operation-Location"]
    operation_id = operation_location_remote.split("/")[-1]

    while True:
        get_handw_text_results = computervision_client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    return get_handw_text_results

def find_number_plate(get_handw_text_results): # detect_text_image(remote_image_url)
    image_list_text = []
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
                line.text = re.sub(r'[^\w\d]+', '', line.text)
                line.text = line.text.replace(" ", "")
                image_list_text.append(line.text)
    return image_list_text #[re.search(r'[A-Z0-9# \-]+', text) for text in image_list_text]



def check_ticket(number_plates): # find_number_plate(detect_text_image(remote_image_url))
    for j in number_plates:
        for i in eligible:
            if i == j:
                return True
    return False


def check(found_text):
    if check_ticket(found_text):
        return "Authorized!", 200
    else: 
        return "Not authorized!", 401


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    body = req.get_json()

    if 'remote_image_url' not in body:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a remote_image_url in the request body for a response.",
             status_code=400
        )

    remote_image_url = body['remote_image_url']

    get_handw_text_results = detect_text_image(remote_image_url)
    found_text = find_number_plate(get_handw_text_results)

    result, status_code = check(found_text)

    func.HttpResponse.mimetype = 'application/json'
    return func.HttpResponse(json.dumps({"result": result}), status_code=status_code)
