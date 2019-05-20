FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
EXPOSE 53
#RUN apt-get update && apt-get install -y python && apt-get install -y iputils-ping && apt-get install -y dnsutils && apt-get install -y vim && apt-get install -y supervisor && apt-get install -y net-tools
RUN apt-get update && apt-get install -y python && apt-get install -y supervisor
RUN mkdir /DNSoTLS
COPY DNS_o_TLS-TCP.py /DNSoTLS
COPY cloudflare-dnscom.crt /DNSoTLS
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]


