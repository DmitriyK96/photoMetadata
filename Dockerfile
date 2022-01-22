FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY templates/* ./templates/

COPY run.py .

CMD [ "python", "run.py" ]
