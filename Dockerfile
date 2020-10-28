FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3