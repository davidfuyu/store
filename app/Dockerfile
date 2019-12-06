FROM python:3.6

# RUN apt-get update; apt-get install npm -y; npm install @vue/cli -g
# 
# WORKDIR /app
# EXPOSE 5000
# 
# COPY requirements.txt /app
# RUN pip install -r requirements.txt
# 
# COPY main/app.py /app/main
# CMD python main/app.py


RUN apt-get update; apt-get install npm -y; npm install npm -g; npm install @vue/cli -g

EXPOSE 5000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD python /app/main/app.py
