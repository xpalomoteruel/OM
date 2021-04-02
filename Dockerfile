FROM python:3

WORKDIR .

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache

COPY . .

CMD ["python", "app.py"]