# synerdo-api

## `.env` file
```
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SECRET_KEY=None
```


## Start project with Docker compose

```bash
docker compose up --build -d
```

```bash
docker compose exec api bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser"
```

## Start project with Docker

```bash
docker build -t synerdo-api .
```

```bash
docker run --env-file .env -p 8000:8000 -d IMAGE
```

### Admin panel test

```bash
docker exec -it CONTAINER_ID python manage.py migrate
```

```bash
docker exec -it CONTAINER_ID python manage.py createsuperuser
```


## Start project local

### Set environment and install dependencies
```bash
python -m venv venv
```

```bash
source venv/bin/activate            # Linux
```

```bash
.\venv\Scripts\activate             # Windows
```

```bash
pip install -r requirements.txt
```

### Run

```bash
cd synerdo/
```

```bash
./manage.py runserver
```
Starting development server at http://127.0.0.1:8000/


### Admin panel test

```bash
./manage.py migrate
```

```bash
./manage.py createsuperuser
```

login and test at http://127.0.0.1:8000/admin/
