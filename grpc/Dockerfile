FROM alpine:latest
LABEL maintainer='h-makihara<macky0325@gmail.com>'

ARG VERSION
ARG http_proxy=$http_proxy
ARG https_proxy=$https_proxy

# system
RUN apk update \
    && apk upgrade \
    && apk add -U --no-cache perl openssl \
    && apk add --no-cache git \
                          curl \
                          bash \
                          mysql-client \
                          make \
                          linux-headers \
                          build-base \
                          protobuf \
                          go \
                          musl-dev

# go gRPC setup
RUN go get -u google.golang.org/grpc \
    && go get -u github.com/golang/protobuf/protoc-gen-go

#RUN pip3 install --upgrade pip \
#    && pip3 install pymysql \
#    && pip3 install cython \
#    && pip3 install grpcio-tools
