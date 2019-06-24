FROM nikolaik/python-nodejs:latest
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE timeline.settings.docker

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin curl nginx supervisor

RUN pip install uwsgi

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN mkdir frontend
COPY frontend/yarn.lock frontend/package.json frontend/

RUN cd frontend && yarn install

COPY . .

RUN cd frontend && yarn build

EXPOSE 80

CMD ["supervisord", "-n"]