# synerdo-api

## Start project with Docker compose

```bash
docker compose up --build -d
```

```bash
docker compose exec api bash -c "python manage.py migrate"
```


## Start project local

### Launch database
```bash
docker compose -f db_compose.yml up -d
```
In `.env` file set DATABASE_HOST=localhost

### Set environment and install dependencies
```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### Run

```bash
cd synerdo/
```

```bash
./manage.py migrate
```

```bash
./manage.py runserver
```

Starting development server at http://127.0.0.1:8000/
