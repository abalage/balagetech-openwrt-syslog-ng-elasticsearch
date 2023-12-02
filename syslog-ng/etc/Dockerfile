FROM balabit/syslog-ng:4.5.0

COPY syslog-ng/ /etc/syslog-ng/

ENV PYTHONPATH=$PYTHONPATH:/etc/syslog-ng/python/

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install --no-install-recommends -y python3-publicsuffix2 && rm -rf /var/lib/apt/lists/*

RUN syslog-ng-update-virtualenv -y
RUN /var/lib/syslog-ng/python-venv/bin/python3 -m pip install publicsuffixlist

VOLUME /var/log

ENTRYPOINT ["/usr/sbin/syslog-ng", "-Fe"]
