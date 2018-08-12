FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn -w $(nproc --all) -b :80 main:app