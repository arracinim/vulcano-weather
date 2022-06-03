FROM python:3.7-slim

ENV APP_HOME /app
ARG DB_NAME
ARG DB_HOST
ARG DB_PORT
ARG DB_USER
ARG DB_PASSWORD
ARG HOST
ARG PORT

WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

ENTRYPOINT DB_NAME=$DB_NAME DB_HOST=$DB_HOST DB_PORT=$DB_PORT DB_USER=$DB_USER DB_PASSWORD=$DB_PASSWORD uvicorn main:app --host $HOST --port $PORT
