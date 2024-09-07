FROM python:3-alpine3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.t
EXPOSE 3000
CMD ["python", "./splash.py"]