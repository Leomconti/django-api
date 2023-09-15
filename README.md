# Django Rest Framework Api

# Installing the Requirements and Running the API

1. To install the dependecies needed to run the project please run the command, preferreably in a virtual environment, I use PyEnv. The python version it was developed in is 3.11

```
pip install -r requirements.txt
```

-   Be sure you are in the **/api_seazone** directory to run the commands from now on

2. First we need to setup the database migrations, so we can work with data. The following commands will add the django models created to the database, and make the migration. For simplicity, the database we're using is SQLite, so there's no complexity to spin up a docker container with a database. But in production, it would be ideal to work with another relational database, like MySQL or PostgreSQL.

```
python manage.py makemigrations
python manage.py migrate
```

3. To run the API and check if everything was done correctly:

```
python manage.py runserver
```

This will start the server in your browser, check the console for the port it started on, usually is 8000 if available

4. To test out the api, we're using **fixtures**, they are already included in the repository, in /api_seazone/fixtures, but you can make your own if you want to. In the fixture, all fields need to be in the json, including those wit auto_now_add set to True

To insert fixtures in the database:

```
python manage.py loaddata fixtures/imoveis_fixture.json
python manage.py loaddata fixtures/anuncios_fixture.json
python manage.py loaddata fixtures/reservas_fixture.json
```

5. To run the unit tests I created, to check if everything is set up correctly, just run:

```
python manage.py test
```

<br>
<br>
<br>
<br>
<br>

# Documentation

-   For better modularization, control and maintenance, each API is contained on its on app in django

-   To test it out, just start the server and when you search for the endpoint, you can use django rest frameworks interface to interact with it

## Following is the documentation and explanation for each endpoint

### Anuncios

URL: /anuncios/

-   POST /anuncios/: Create a new anuncio.
-   GET /anuncios/: Retrieve a list of all anuncios.
-   GET /anuncios/`<int:pk>`/: Retrieve details of a specific anuncio by its primary key.
-   PUT/PATCH /anuncios/`<int:pk>`/: Update a specific anuncio by its primary key.
-   DELETE /anuncios/`<int:pk>`/: Delete a specific anuncio by its primary key.

### Imoveis

URL: /imoveis/

-   POST /imoveis/: Create a new imovel.
-   GET /imoveis/: Retrieve a list of all imoveis.
-   GET /imoveis/`<int:pk>`/: Retrieve details of a specific imovel by its primary key.
-   DELETE /imoveis/`<int:pk>`/: Delete a specific imovel by its primary key.

### Reservas

URL: /reservas/

-   POST /reservas/: Create a new reserva.
-   GET /reservas/: Retrieve a list of all reservas.
-   GET /reservas/`<int:pk>`/: Retrieve details of a specific reserva by its primary key.
-   DELETE /reservas/`<int:pk>`/: Delete a specific reserva by its primary key.
