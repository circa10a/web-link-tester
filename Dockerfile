FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /app
RUN bash /app/install_deps.sh
