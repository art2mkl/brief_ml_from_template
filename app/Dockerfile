FROM python:3.9

COPY . /app/app

WORKDIR /app/app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]