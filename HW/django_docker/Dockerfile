FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /django_docker
COPY requirements.txt /django_docker/
RUN pip install -r requirements.txt
COPY . /django_docker/ 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
