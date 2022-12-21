FROM python:3

WORKDIR /app/src

COPY . .

COPY supervisord.conf /etc/supervisord.conf

RUN pip install -r requirements.txt

RUN apt update && apt install -y redis

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
