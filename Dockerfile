FROM python:3.8.13-slim-buster

WORKDIR /app
RUN pip install --upgrade pip --no-cache-dir
COPY ./requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY ./portfolio_app ./

COPY ./entrypoint.sh ./
ENTRYPOINT ["sh","/app/entrypoint.sh"]