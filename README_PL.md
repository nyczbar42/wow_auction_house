# Skrypty do Pobierania i Przetwarzania Danych Aukcji z World of Warcraft

Ten projekt zawiera skrypty do pobierania danych aukcji z gry World of Warcraft, przetwarzania ich i zapisywania wyników do pliku. Skrypty wykorzystują API Battle.net do pobrania informacji o aukcjach i cenach przedmiotów na serwerach EU.

## Skrypty

### `run_all.sh`

Ten skrypt bashowy uruchamia wszystkie poniższe skrypty w odpowiedniej kolejności.

1. Sprawdza, czy plik ```access_token.json``` istnieje i jeśli nie, uruchamia ```get_token.py``` w celu pobrania tokena.
2. Uruchamia ```get_auctions.py```, aby pobrać dane aukcji.
3. Uruchamia ```parse_auctions_json.py```, aby przetworzyć dane i zapisać wyniki do ```item_prices.txt```.

#### Jak uruchomić:
1. Zarejestruj aplikację na stronie Blizzard Developer Portal i uzyskaj klucz API (Client ID oraz Client Secret).
2. Wprowadź w pliku ```get_token.py``` swóje Client ID oraz Client Secret do zmiennych ```client_id``` i ```client_secret```.
3. Przedmioty, których ceny chcesz sprawdzić znajdują się w pliku ```parse_auctions_json.py```
4. Upewnij się, że masz zainstalowanego Pythona oraz biblioteke ```requests``` i nadałeś plikowi ```run_all.sh``` uprawnienia do wykonywania:
   ```sh
   chmod +x run_all.sh
5. Uruchom skrypt:
   ```sh
   ./run_all.sh

Skrypty utworzą plik ```item_prices.txt``` i zapiszą w nim ceny przedmiotów.
Poniżej znajdują się opisy skryptów i instrukcja ich wykonania w przypadku nie korzystania ze skryptu ```run_all.sh``` 

### `get_token.py`

Ten skrypt pobiera token dostępu do API Battle.net i zapisuje go do pliku `access_token.json`. Token jest wymagany do autoryzacji zapytań do API.

#### Jak uruchomić:
1. Upewnij się, że masz zainstalowanego Pythona.
2. Uruchom skrypt:
   ```sh
   python3 get_token.py


### `get_auctions.py`

Ten skrypt pobiera dane aukcji z API Battle.net i zapisuje je do pliku ```eu_auctions.json```. Skrypt używa tokenu dostępu z pliku ```access_token.json```.

#### Jak uruchomić:
1. Upewnij się, że masz zainstalowanego Pythona oraz plik ```access_token.json``` zawierający aktualny token.
2. Uruchom skrypt:
   ```sh
   python3 get_auctions.py

### `parse_auctions_json.py`

Ten skrypt przetwarza dane z pliku ```eu_auctions.json``` i zapisuje najniższe ceny przedmiotów do pliku ```item_prices.txt```. Skrypt wyciąga ceny przedmiotów i ich nazwy w formie czytelnej dla użytkownika.

#### Jak uruchomić:
1. Upewnij się, że masz zainstalowanego Pythona oraz plik ```eu_auctions.json``` zawierający aktualne dane aukcji.
2. Uruchom skrypt:
   ```sh
   python3 parse_auctions_json.py

## Wymagania:

- Python 3.x
- Biblioteki Python: requests (do zainstalowania za pomocą pip install requests)
- Dostęp do Internetu (do pobierania danych z API Battle.net)

## Uwagi
- Skrypty zakładają, że masz aktywne konto Battle.net i odpowiednie uprawnienia do korzystania z API.
- Token dostępu jest ważny przez określony czas, więc może być konieczne jego odświeżenie w razie potrzeby.