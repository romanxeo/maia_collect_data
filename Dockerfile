FROM python:3.10

WORKDIR /app

ADD ./requirements.txt .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8001