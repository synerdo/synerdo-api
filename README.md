# synerdo-api

## Start project local

### Set environment and install dependencies
```bash
python -m venv venv
```

```bash
source venv/bin/activate            # Linux
```

```bash
.\venv\Scripts\activate             # Windows (not recommended)
```

```bash
pip install -r requirements.txt
```

### Environment Variables
Create `.env` file:
```
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
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
