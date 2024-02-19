FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8080", "application:application"]
