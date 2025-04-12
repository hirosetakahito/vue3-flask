FROM python:3.12-slim

WORKDIR /app
ENV FLASK_APP=app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["flask", "run", "-h", "0.0.0.0"]
