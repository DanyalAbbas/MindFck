FROM python:3.12

WORKDIR /Mindfck-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ML_Models ./ML_Models
COPY ./templates ./templates
COPY ./app.py .


CMD [ "python3",  "./app.py"]