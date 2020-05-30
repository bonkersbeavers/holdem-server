FROM python:3

COPY ./ /home/poker-server/

WORKDIR /home/poker-server/

RUN pip3 install -r requirements.txt

EXPOSE 5000