
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install gunicorn==20.1.0


COPY . .


RUN python manage.py collectstatic --noinput --settings=NEWS.settings


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "NEWS.wsgi:application"]
