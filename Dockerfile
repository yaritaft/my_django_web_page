FROM python:3.6.8

RUN mkdir -p /app
RUN mkdir -p /app/static
ADD requirements.txt app
WORKDIR /app
RUN pip install --upgrade pip==19.3
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input 
CMD ["gunicorn", "-w", "1", "--bind", ":8000", "mysite.wsgi:application"]