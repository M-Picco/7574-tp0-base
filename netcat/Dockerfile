# from https://github.com/subfuzion/docker-netcat/tree/master
FROM alpine:edge as BUILD
RUN apk add --no-cache netcat-openbsd
ENTRYPOINT [ "nc" ]