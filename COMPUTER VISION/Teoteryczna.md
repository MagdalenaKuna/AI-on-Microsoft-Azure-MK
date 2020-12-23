# Część teoretyczna

Wraz z postępem dotyczącym ciagle rozwijających się metod uczenia w oparciu o dane opisowe zaczęliśmy chcieć więcej. Obecnie bardzo obiecującą gałęzią dotyczącą zarówno sztucznej inteligencji jak i obrazów stało się inteligentne ich rozpoznawanie znane pod pojeciami takimi jak cognitive vision czy image processing. W Azure istnieje wiele mozliwości przetwarzania obrazów jednakze dziś skupimy się na trzech - tych bardziej znanych i dla nas dostepnych oraz prostych do wykorzystnia. 

Wszystkie te rowiązania sa częścią Cognitive Serwises dostępnych na portalu Azure, które służą do różnorodnego rozpoznawania i przetwarzania mowy, pisma, obrazów, dźwięków i wielu innych.

## Computer Vision API

#### <ins>Intro</ins>:
Computer Vision API można rozumieć dwojako - pierwsze jako osobny serwis o tejże nazwie bądź serwisy takie jak Face API czy Emotions API. Te dwa ostatnie jak sama nazwa wskazuje związane są głównie z rozpoznawaniem twarzy na zdjęciach oraz emocji. W Face API twarz nie jest tylko rozpoznawana i obzaczana jako boxbounding ale także w tym serwisie można stworyć grupę składającą sie z kilku osób, gdzie każda z osób moze mieć własny set skłądający się z kilku zdjęć. Tworzy się to w celu przetwarzania ich by można było podjąć się prób identyfikacji twarzy czy znalezienia podobieństw w twarzach oraz by można było wykluczyć daną twarz np. z kanonu podejrzanych. Twarz moze być także bardziej szczegółowo opisana poprzez podanie dokładnej lokalizacji szczegółowych parametrów tej twarzy jak lokalizacja nosa, oczu, brwi i innych a nawet w jakiej przestrzeni 3D ta twarz się znajduje. Emotions API także pozwala zlokalizować twarz jednak zamiast identyfikacji twarzy i grupowania stara się sklasyfikować emocje występujące na tej twarzy. Z przedziału od 0 do 1 nadaje wartości poszczególnych emocji, które potrafi zanalizować. Emocje te to radość, strach, smutek, znużenie i jeszcze kilka innych. Im wartość jest bliższa wartości 1 tym większe prawdopodobieństwo, że dana osoba odczuwa własnie taką emocję. Wracając jednak do najbardziej rozbudowanego serwisu czyli Computer Vision API możemy takze wykryć tam twarz danej osoby - poznać lokalizacje tej twarzy jednak to rozpoznawanie kończy się na lokalizacji czyli nie jest tak szczegółowe jak w dwóch opisanych wyżej serwisach. Za to ten servis ma bardzo wiele innych ciekawych możliwości. Można tutaj wgrać bardzo różne zdjecia a wynikowo dostaje się opis tych zdjęć, czyli co się znajduje i dzieje na tym zdjęciu. Oprócz tej możliwości można zdjęcie skadrować na różne sposoby - podając odpowiednie wartości - i skalibrować, przykładowo zdjęcie można zmiejszych lub zwiększych dbając, głównie skupiając się na obszarze prez nas potrzebnym. Z obrazu można także wyciągnąć, wydobyć tekst zarówno drukowany (case sensitive!) jak i pisany ręcznie. Podany jest wtedy język, jeżeli jest możliwość jego sklasyfikowania, oraz lokalizacje tego tekstu oraz jest wartość. Wszystkie wyzej opisane wartosci jakie z tych wszystkich serwisów można pozyskać dostaje się wynikowo w formacie JSON, gdzie wsystko jasno i wyraźnie jest opisane. 
    
#### <ins>Use cases</ins>:
* na policji w celu rozpoznawania przestępców/ szukania na kamerach zaginionych/ rozpoznawania zmarłych

* rozpoznawanie pracowników w firmach + połaczenie tego z kontrolą dostępu, np czy dana grupa techniczna ma dostęp w firmie do serwerowni
    
* rozpoznawanie emocji osób wchodzacych do banku/ samolotu/ parlamentu/ szkoły - system prewencji, zapobieganie przykrym wydarzeniom
    
* rozpoznawanie depresji poprzez analizę emocji 
    
* segregowanie/klasyfikowanie obrazów w celu dalszej ich obróbki
    
* rozpoznawanie tekstu - starych manuskryptów
    
#### <ins>How to</ins>:
We wszystkich wymienionych serwisach należy mieć aktywną usługę - subskrypcję na portalu Azure. Do Face API oraz Emotion Api najlepiej połaczyć się za pomoca REST API, a korzystając z Computer Vision API najlepiej skorzystać z konsoli aby uzyskać ważne dla nas dane oraz dostosować ustawienia. 
        
Niezależnie czy jest to detekcja rzeczy na obrazie, tekstu, szukania na obrazie np. twarzy, detekcji punktów szczególnych na obrazie czy innych możliwości pierwsze 1000 jednostek na miesiac jest darmowe, następnie kolejne 1001-5000000 jednoski na miesiac są płatke 1,5$ a każde kolejne ponad - 0.60$


## Custom Vision

#### <ins>Intro</ins>:
Serwis pozwala sklasyfikować zdjęcia oraz można wykryć gdzie znajsuje się ważny dla nas obszar na zdjęciu. Początkowo należy wybrać zbiór zdjęć, które należy odpowiednio otagować, tagowanie już robimy korzystając z naszego serwisu. Można w serwisie wybrać czy chcemy zrobić detekcję czy klasyfikację. Nastepnie należy korystając z serwisu wytrenować nasz model - robi się to bardzo prosto, po prostu naciskając przycisk. Nie trzeba wgrywać bardzo dużo zdjęć jednakże minimalna ich ilość, aby algorytm działał poprawnie to 5. Dzieje się tak dlatego prawdopodobnie, że dany model w Azure jest po prostu douczany o nasze dane. Następnie należy zapoznać się z wynikami uczenia i jeżeli sa one dla nas satysfakcjonujące model należy opublikować. Tak opublikowany model możemy teraz poddać procesowi testowania. Przy testowaniu dostaniemy opowiednie parametry, czyli zapoznamy się czy nas model także dobrze działa dla tych danych. Połaczenie można zrobić za pomocą protokołu HTTP. Należy uwazać, żeby w procesie autentyfikacji i pubikowania nie podać wrażliwych danych.

#### <ins>Use cases</ins>:
* wszelakie rozpoznawanie jednego obiektu od drugiego np. czerwonych buletek od zielonych puszek
        
* rozpoznawanie roślin jadalnych od trujących np. grzybów
    
* sprawdzanie czy produkt nie ma uszkodzonych części w danym produkcie
    
* segregacja typów ubrań czy butów by potem szybciej wyszukiwać ważny dla nas produkt
    
#### <ins>How to</ins>:
Należy zalogować się na portal obsługujący tę funkcjonalność, który jest bardzo prosty w obsłudze i intuicyjny. Należy mieć jednak zdefiniowaną grupę domową w której chcemy odpalić nasz projekt a reszta jest już bardzo prosta, tylko wgrać, wytrenować opublikować i patrzeć jak wsystko działa na 100 % :). Do połaczenia z tym serwisem można użyć konsoli Azura. 

Bezpłatnie są dostępne 2 transakcje na sekundę, max godzina trenowania na miesiąc i max liczba projektów to 2, do 5000 obrazów na projekt oraz do 10 000 prognoz. Wersja standardowa zakłada 10 transakcji na sekundę za 1,7$ za 1000 transakcji, max liczba projektów 100, szkolenia/uczenie 17$ za godzinę obliczeniową, i magazyn obrazów do 6MB każdy, a kosztuje to 0.6$ za 1000 obrazów. Ceny podane dla East US 2.



## Video Indexer

#### <ins>Intro</ins>:
Sewis pomaga uporządkować - zaindeksować wiele plików wideo tak aby łatwiej było można znaleźć odpowiednie dla siebie materiały. Video indekser korzysta z takich możliwości jak rozpoznawanie twarzy, napisów, obiektów czy nawet emocji na zdjęciu. Do nauki platforma pozwana na zaindeksowanie filmów o łączej długości 600 minut a API Video indeksera można używać 2400 minut. Serwis daje możliwość obsługi wielu formatów wideo, plik można też wgrać jako URL jednakże nie można go wgrać np. z youtube. Poprzez wyszukiwarkę można wyszukać odpowiednie sceny w wideo. Sceny z wideo są też dzielone na mniejsze części - zdjęcia oraz wyszczególnione są kluczowe klatki w każdym wideo. Tagi, którymi oznaczone są klatki można takze edytować oraz tworzyć ich miniatórki.


#### <ins>Use cases</ins>:
* do platform e-learningowych do dokładnego okreslenia przeznaczenia filmu oraz zakresu jaki jest w nim poruszony, co pozwoli uczacym wybrać filmy, które ich konketnie interesują
        
* do wielu platform, gdzie użytkownicy moga wgrywać swoje filmy w celu wykrywania nieprzyzwoitych treści i kasowania danego materiału

* analizowanie kto wchodzi i wychodzi z danego budynku, zaindeksowanie dniami danych nagrań w celu szybszego znalezienia ważnego nagrania
    
#### <ins>How to</ins>:
Należy zalogować się na portal video indeksera, dostosować odpowiednio autoryzację - połaczyć się z indekserem a naszym kontem azurowym

Darmowe jest 10 godzin na stronie użytkownika i 40 w API. Video Indekser zakłada uzywanie innych takze serwisów, które mają osobne ceny więc trzeba dokładnie sprawdzić cenowo co będzie nam do danego projektu potrzebne, więc ceny moga być różne przy różnych projektach jednak nie jest je trudno oszacować, bo kazdy inny serwis ma także rozbudowaną tabele cennikową. 

