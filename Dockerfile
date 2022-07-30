FROM python:3.8.13-slim-buster

WORKDIR /app

COPY ./portfolio_app ./

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./entrypoint.sh ./

ENTRYPOINT ["sh","/app/entrypoint.sh"]