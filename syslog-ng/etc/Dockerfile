FROM balabit/syslog-ng:4.5.0

COPY syslog-ng/ /etc/syslog-ng/

# Only for referencing what env values we rely on
# One should overwrite them via ConfigMap or Secret
ENV REMOTE_HOST="127.0.0.1"
ENV REMOTE_PORT="9200"
ENV REMOTE_SCHEME="http"
ENV REMOTE_HOST_AND_PORT="${REMOTE_HOST}:${REMOTE_PORT}"
ENV REMOTE_USER="user"
ENV REMOTE_PASS="password"
ENV DNS_SERVER="1.1.1.1"
ENV NETWORK_NAME="Balage Home"

ENV PYTHONPATH=$PYTHONPATH:/etc/syslog-ng/python/

VOLUME /var/log

# /etc/syslog-ng/GeoLite2-City.mmdb
