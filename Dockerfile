FROM python:3.7-slim

ENV APP_HOME /app

ENV DB_NAME $db_name
ENV DB_HOST $db_host
ENV DB_PORT $db_port
ENV DB_USER $db_user
ENV DB_PASSWORD $db_password
ENV HOST 0.0.0.0
ENV PORT 80

WORKDIR $APP_HOME
COPY . ./

RUN echo $DB_NAME
RUN pip install -r requirements.txt

ENTRYPOINT DB_NAME=$DB_NAME DB_HOST=$DB_HOST DB_PORT=$DB_PORT DB_USER=$DB_USER DB_PASSWORD=$DB_PASSWORD uvicorn main:app --host $HOST --port $PORT
