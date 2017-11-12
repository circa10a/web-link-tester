FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /app
RUN pip install -r /app/requirements.txt
EXPOSE 5000
