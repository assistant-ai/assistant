FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "assistant.action"]
