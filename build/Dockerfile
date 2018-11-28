FROM python:3.6-alpine

RUN mkdir -p /app && mkdir -p /deploy

COPY requirements.txt /deploy
RUN apk --update add --virtual build-base \
  && python3 -m ensurepip \
  && pip install --upgrade pip \
  && pip install -r /deploy/requirements.txt

WORKDIR /app
COPY ./app /app/

EXPOSE 5000

CMD ["gunicorn", "--config", "/app/gunicorn.cfg", "server:app"]

