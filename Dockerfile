FROM python:3.10
MAINTAINER Simon Golovinskiy 'example@mail.ru'

LABEL authors="wasa"
RUN mkdir -p /usr/src/app/wrkdir
WORKDIR /usr/src/app/wrkdir

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8080


CMD ["python", "run.py"]