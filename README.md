## How to run this demo

0. clone

```bash
git clone https://github.com/CNLHC/django-upload-demo 
```

1. ensure cwd and create media dir

```bash
cd django-upload-demo;
mkdir -p media/uploads;
```

2. install dependencies

```bash
python3 -m pip install django
```

3. migrate database

```bash
python3 manage.py migrate
```

5. run

```bash
python3 manage.py runserver 1234
```

6. check front-end page at `http://localhost:1234/static/demo.html`
