FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

COPY requirments.txt /app/
COPY app.ini /app/

RUN pip3 install -r requirments.txt
COPY ./app /app