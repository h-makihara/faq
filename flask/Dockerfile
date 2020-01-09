# flask Dockerfile
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
    && apk add --no-cache --virtual .base\
                                    git \
                                    mysql-client \
                                    python3 \
                                    make \
                                    linux-headers \
                                    build-base

RUN apk add --no-cache --virtual .on-build \
                                    curl \
                                    bash 

RUN apk add --no-cache --virtual .build-deps \
                                 gcc \
                                 musl-dev \
                                 python3-dev \
                                 protobuf \
                                 go

RUN export GOPATH=/usr/local/bin
RUN go get github.com/fullstorydev/grpcurl
RUN go install github.com/fullstorydev/grpcurl/cmd/grpcurl

# test python client
RUN pip3 install --upgrade pip \
    && pip3 install prettytable \
    && pip3 install pymysql \
    && pip3 install cython \
    && pip3 install grpcio-tools
