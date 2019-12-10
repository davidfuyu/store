FROM python:3.6

RUN apt-get update; apt-get install npm -y; npm install npm -g; npm install @vue/cli -g

EXPOSE 50000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD python /app/main/app.py
