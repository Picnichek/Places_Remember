FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "places_remember_project/manage.py", "runserver", "0:8000"]