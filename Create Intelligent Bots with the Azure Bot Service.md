# **QnA Maker**
# *I. Intro*
Jest to serwis pomagający tworzyć proste wzorce komunikacyjne, które są skonstruowane jako pytanie – odpowiedź i tak w kółko. Serwis ten wykorzystywany jest często, aby współpracując z innymi serwisami stworzyć bota odpowiadającego na pytania. Należy samemu stworzyć bazę par pytanie i odpowiedz, jakie bot mógłby udzielić. Często taka baza jest wzorowana na FAQ danej strony. Pytanie jednak można zadać na wiele różny sposów, co może być problemem. Jednakże można to także naprawić używając serwisów do przeznaczonych do przetwarzania języka naturalnego. Nalezy pamiętać, że pytanie o takim samym znaczeniu ale innym wydźwięku może zadać użytkownik więc należy na tę okoliczność także się ubezpieczyć. Następnie należy wytrenować nasza bazę, gdzie buduje się model oparty o język naturalny. Po wytrenowaniu dobrą praktyką jest przetestować przygotowany model zadając mu pytania i sprawdzając otrzymane odpowiedzi. Na koniec należy opublikować bazę i połączyć się z nią poprzez aplikację używając REST API. Aby się połączyć należy użyć ID, nazwy endpointu i klucza autoryzacyjnego. 
Jeśli chodzi o cenę to bezplatnie serwis obsługuje 3 transakcje na sekundę, trzy dokumenty do 1 MB, 100 transakcji na minute i 50 000 na miesiąc, wersja standardowa -  3 transakcje na sekundę, 100 transakcji na minutę i za 8,433 euro nieograniczona ilość dokumentów do zarządzania.

# *II. Use Case*
- dla wsystkich firm, żeby dopasować spotkanie automatycznie
- dla firm, żeby przedstawić oferty i rozwiązać łatwiejsze problemy
- aby wstępnie określić problem pacjenta
- aby odciążyć dyskozytorów karetek, zażądzając zgłoszeniami i prowadząc wstępny wywiad
- aby zautomatyzować sklep internetowy

# *III. How to*
Poczatkowo należy przygotowac baze wiedzy. Natepnie baze tą przenieść do specjalnie do tego stworzonego portalu czyli Q&A Maker portal, gdzie bazę należy stworzyć, wytrenować, opublikować i tak także można nią zarządząć, czy ją udoskonalać. Są dwie możliwości stworzenia tego portalu, albo tworząc zasób Q&A Maker w Azure portal albo storzyć baze wiedzy a następnie ten zasób. Ze wszystkich dostepnych źródeł należy zebrać dane, z których należy stworzyć bazę par pytanie-odpowiedź. 

# **Azure Bot Service**
# *I. Intro*
Jest to serwis tworzący bota, który może obsługiwać wiele użytkowników w tym samym czasie. Obsługuje on różne kanały. Jest to interfest dla bazy par pytanie-odpowiedź, które może być stworzona przy pomocy serwisu Q&A Maker. 

# *II. Use Case*
- wszystkie powyżej (traktuję je jako serwisy powiązane, które już tworzą jeden produkt)
- pomoc w doborze rzeczy do kuchni, łazienki, kolorów
- pozwala znaleźć sklepy danej firmy i prowadzi do nich
- pomoc psychiczna i rozpoznanie psychicznych chorób
- bot(robot) który rozmawia z człowiekiem, dotrzymuje mu towarzystwa 

# *III. How to*
Najprostrzym rozwiązaniem, mając stworzoną bazę w opisanym powyżej serwisie, jest przejście do serwisu Q&A maker i tam stworzenie botu w oparciu o opublikowaną bazę wiedzy. Jest to kilka kliknięć. Po tym pojawia się serwis o nazwie Azure Bot Serwis, gdzie można dalej zarzadzać botem, czyli dodać własny kod, przetestować bota, skonfigurować go wedle potrzeb, poddawać analizie dane otrzymywane i wiele więcej. Ważne jest aby podłączyć bota do różnych mediów przez które może kontaktować się użytkownik, takich jak strona internetowa, email czy inne. 
Jeśli chodzi o cenę to w tym serwisie płaci się za kanały. Kanały standardowe czyli usługi firmay Microsoft (Teams, Skype, Cortana) oraz z publicznym interfejsem API botów (Facebook, Slack) i inne (patrz dokumentacja Bot Service) są bezpłatne, czyli mają nieograniczoną możliwosć przesyłu komuniktów. Usługi inne niż standowe, czyli premium kosztują 10 000 komunikaów na miesiąc, a za każde 1000 komunikatów należy zapłacić 0.422 euro.

# **Bot Framework Composer**
# *I. Intro*
Serwis tworzy łatwo i szybko zaawansowanego bota bez pisania kodu. Serwis ten pozwala wykorzystać bardzo ciekawe możliwości, przykładowo można wykorzystać concepcję adaptive dialogs, która pozwala wprowadzić do rozmowy pewien kontekst przez co ma możliwość lepiej formować odpowiedzi, stosując przerwania, uczenie maszynowe i wiele więcej. Z adaptive dialogs można także zastosować Language Generation, które to z kolei pozwala bardziej dostosować bota pozwalając stworzyć bota głosowego i bardziej go spersonalizować odpowiednio do potrzeb. Jednakże jest to dużo bardziej złożone narzedzia niż teraz opisane w tych kilku słowach.
Wracając jednak do composera można także go wizualnie dostosować aby był przyjeniejszy do odbioru, pozwala także na ponowne użycie zapisanych wiadomości w paczkach jako JSON lub Markdown, które potem mogą być wykorzystane przez inne sewisy do przetwarzania języka lub w szablonach, np. LUIS

# *II. Use Case*
- do tworzenia spersonalizowanych botów, gdy jest taka potrzeba
- do teatru aby sprzedawać bilety
- do nauki i powtórek może jakiegos specyficznego tematu
- do urzędu aby szybciej załatwiać swoje sprawy i lepiej się przygotowac do spotkania jeżeli musi ono nastąpić
- do spraw, aby poprowadzić nowych użytkowników np. dla użytkowników którzy tworza firmę i prowadzi ich za rekę co trzeba i należy zrobići jakie są możliwości poboczne. 

# *III. How to*
W odróżnieniu do serwisów, z którymi zwykle mieliśmy styczność na platformie Azure, aby skorzystać z Bot Framework Composer, należy poczatkowo pobrac i zainstalować aplikację na własnym komputerze, obsługiwane są takie systemy jak Windows, mocOS i Linux. Możliwe, że przydatny tez będzie Bot Framework Emulator, a warunkiem koniecznym jest posiadanie .NET Core SDK 3.1. W startowym ekranie można zobaczyć menu, w którym są takie zakładki jak Home, Design, Bot Responses, User Input, Notifications, Publish i Skills. Każda z zakładek opisuję z grubsza co robi. Należy stworzyć nowego bota, dodać odpowiednie dane następnie pierwszy szablon pytanie odpowiedz. Należy poeksperymentować żeby poznać możliwości tego narzedzia. Następnie należy stworzyć też dialogi, Są dwa do wyboru – main dialog i child dialog. Child diagog pozwala na stworzenie bardziej zawiłej, ciekawszej komunikacji. Następnie należy stworzyć anatomie dialogu czyli wybrać jeden z kompunentów – LU Recognition lub Trigger, ten drugi wymaga aby okreslić dla niego jaki ma typ: intent recognition, unknown intent, dialog event, activities, custom events. Kazdy z typów ma swój cel oraz możliwości do wykorystania. Ważne jest aby nie zostawiać użytkowników dla których korzystanie z botów nie jest intuicjne i zaimplementować pomoc do bota oraz funckję, gdzie bot może się rozłączyć/wyłączyć. Bota można by także zintegrować z Language Generation, dzięki któremu można bardzije spersonalizować wiadomości, np. dodając wiele możliwośc i przywitań czy innych możliwości. Aby zrobić coś ciekawszego wizualnie można dodac kartę do czatu, która może być ładną formą opieczentowania pewnych informacji czy graficznie coś zaprezentować. Na koniec warto zintegrować swojego bota z serwisem LUIS i opublikowac model. Następnie należy testować i korzystać z bota.
