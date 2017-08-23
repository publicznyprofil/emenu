
# Instalacja #
   1. Pobieramy repozytorium *git clone https://github.com/publicznyprofil/emenu.git*
   2. Jeśli korzystamy z vagranta:
        * *vagrant up*
        * łączymy się przez ssh i uruchamiamy serwer *./manage.py runserver 0.0.0.0:8000* (lub uruchamiamy go z poziomu IDE)
        * łączymy się za pomocą przeglądarki z serwerem pod *http://localhost:8000*
   3. Konfiguracja środowiska gdy nie korzystamy z vagranta:
        * za pomocą *pip* pobieramy zależności znajdujące się w *conf/requirements.txt*
        * tworzymy bazę danych postgres
            * *NAME: **blue_database***
            * *USER: **blue_user***
            * *PASSWORD: **blue_pass***
        * odpalamy migracje *manage.py migrate*
        * ładujemy dane testowe
            * *./manage.py loaddata menu/fixtures/menus.json*
            * *./manage.py loaddata menu/fixtures/dishes.json*
            * *./manage.py loaddata project_blue/fixtures/users.json*
        * uruchamiamy serwer *manage.py runserver*
        * łączymy się za pomocą przeglądarki z serwerem pod *http://localhost:8000*
            
# Dane testowe #
   * Użytkownicy
       * username: **superuser**
       * password: **project_blue**
