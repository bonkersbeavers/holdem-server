FROM python:3

COPY ./ /home/poker-server/

WORKDIR /home/poker-server/

RUN pip3 install -r requirements.txt

CMD ["python3", "./main.py", "server-config.json"]

EXPOSE 5000