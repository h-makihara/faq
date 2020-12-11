# gRPC Dockerfile
FROM alpine:latest
LABEL maintainer='h-makihara<macky0325@gmail.com>'

# copy source and protocols
WORKDIR /app

#ARG VERSION
ARG http_proxy=$http_proxy
ARG https_proxy=$https_proxy

# system
RUN apk update \
    && apk upgrade \
    && apk add -U --no-cache perl openssl \
    && apk add --no-cache --virtual .system-tools \
                                    git \
                                    curl \
                                    bash \
                                    mysql-client \
                                    python3 \
				    py3-pip \
                                    make \
                                    linux-headers \
                                    build-base 
# development
RUN apk add --no-cache --virtual .build-deps \
                                 gcc musl-dev \
                                 python3-dev \
                                 protobuf

RUN pip3 install --upgrade pip \
    && pip3 install prettytable \
    && pip3 install requests \
    && pip3 install pymysql \
    && pip3 install cython \
    && pip3 install grpcio-tools
