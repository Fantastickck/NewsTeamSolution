FROM python:3.9
RUN apt update -y
RUN apt upgrade -y

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]