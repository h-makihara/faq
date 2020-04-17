# frontend Dockerfile
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
                                    make \
                                    linux-headers \
                                    build-base

RUN apk add --no-cache --virtual .on-build \
                                    curl \
                                    bash 

RUN apk add --no-cache --virtual .build-deps \
                                 gcc \
                                 musl-dev \
                                 protobuf \
                                 yarn \
                                 go

RUN export GOPATH=/usr/local/bin
RUN go get github.com/fullstorydev/grpcurl
RUN go install github.com/fullstorydev/grpcurl/cmd/grpcurl

RUN apk add --no-cache --virtual .node \
                                 nodejs \
                                 npm

RUN npm -g config set proxy $http_proxy
RUN npm -g config set https-proxy $https_proxy
RUN npm config list

# Vue.js
RUN npm install -g @vue/cli
# gRPC-WEB
RUN yarn add google-protobuf \
             @types/google-protobuf \
             grpc-web

# material m\icon
WORKDIR /tmp
RUN wget https://github.com/google/material-design-icons/releases/download/3.0.1/material-design-icons-3.0.1.zip
RUN unzip material-design-icons-3.0.1.zip
RUN cp -R material-design-icons-3.0.1/iconfont /app/src/assets/

# angular
#RUN npm install -g webpack \
#                   webpack-dev-server \
#                   webpack-contrib/mini-css-extract-plugin \
#                   chalk \
#                   shelljs \
#                   ora \
#                   @angular/cli
#WORKDIR /app
#RUN ng new angular-app --routing --style scss

