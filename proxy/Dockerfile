FROM envoyproxy/envoy-alpine:latest
RUN apk update
COPY envoy.yaml /etc/envoy.yaml
CMD /usr/local/bin/envoy -c /etc/envoy.yaml
