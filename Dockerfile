FROM python:3

WORKDIR /app

# temporary hack, this is not very safe xD
COPY . .

RUN pip3 install -r requirements.txt