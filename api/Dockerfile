FROM alpine:latest
LABEL maintainer='h-makihara<macky0325@gmail.com>'

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
                                    build-base 
RUN apk update \
    && apk upgrade \
    && apk add --no-cache --virtual .build-deps \
                                    make \
                                    linux-headers \
                                    gcc musl-dev \
                                    python3-dev

RUN pip3 install --upgrade pip \
    && pip3 install prettytable \
    && pip3 install pymysql \
    && pip3 install flask \
    && pip3 install request \
    && pip3 install jsonify \
    && pip3 install make_response
