FROM python:3.6.8

RUN mkdir -p /app
RUN mkdir -p /app/static
ADD requirements.txt app
WORKDIR /app
RUN pip install --upgrade pip==19.3
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "1", "-k", "gevent", "-b", "0.0.0.0:8000", "mysite.wsgi:application"]
