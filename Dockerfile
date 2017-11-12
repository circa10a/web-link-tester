FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
COPY . /app
RUN pip install -r /app/requirements.txt
