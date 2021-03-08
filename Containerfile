FROM python:3.9.1-alpine3.13 

ENV GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
ENV GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1

RUN apk add build-base linux-headers openssl-dev zlib-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


CMD [ "python", "main.py" ]

EXPOSE 50051
