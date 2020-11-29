# balagetech-openwrt-syslog-ng-elasticsearch
Monitoring home network traffic with OpenWRT, Syslog-ng and Elasticsearch

This repo contains a complete configuration for monitoring home network with OpenWRT and syslog-ng and Elasticsearch Security.

The following components are implemented:
 - connection tracking events by ulogd2
 - DNS logs either by dnsmasq or unbound (preferred)
 - fail2ban events added as alerts

###Contents:
```
.
├── LICENSE
├── README.md
├── elasticsearch
│   └── template-network.json
├── openwrt
│   └── etc
│       ├── config
│       │   ├── dhcp
│       │   └── unbound
│       └── ulogd.conf
└── syslog-ng
    └── etc
        ├── GeoIP.conf
        ├── apparmor.d
        │   └── local
        ├── fail2ban
        │   └── fail2ban.conf
        ├── syslog-ng
        │   ├── conf.d
        │   ├── patterndb.xml
        │   └── syslog-ng.conf
        └── unbound
            └── unbound.conf
```

## Server extra for unbound on OpenWRT
Add this to "Services -> Recursive DNS -> Files -> Edit: Server"
```

# Log to syslog(3) if yes. The log facility LOG_DAEMON is used to
# log to, with identity "unbound". If yes, it overrides the logfile.
use-syslog: yes

# print UTC timestamp in ascii to logfile, default is epoch in seconds.
log-time-ascii: yes

# print one line with time, IP, name, type, class for every query.
log-queries: yes
```

Further information could be found in the website referred in repo details.

