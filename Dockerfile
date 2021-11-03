FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
