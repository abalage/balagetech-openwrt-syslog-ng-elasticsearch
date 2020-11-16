# balagetech-openwrt-syslog-ng-elasticsearch
Monitoring home network traffic with OpenWRT, Syslog-ng and Elasticsearch

This repo contains a complete configuration for monitoring home network with OpenWRT and syslog-ng and Elasticsearch Security.

The following components are implemented:
 - connection tracking events by ulogd2
 - DNS logs either by dnsmasq or unbound (preferred)
 - fail2ban events added as alerts

###Contents:
```

├── LICENSE
├── README.md
├── elasticsearch
│   └── template-network.json
├── openwrt
│   └── etc
│       └── ulogd.conf
└── syslog-ng
    └── etc
        ├── GeoIP.conf
        ├── apparmor.d
        │   └── local
        │       └── sbin.syslog-ng
        ├── fail2ban
        │   └── fail2ban.conf
        ├── syslog-ng
        │   ├── conf.d
        │   │   ├── common.conf
        │   │   ├── network-dnsmasq.conf
        │   │   ├── network-fail2ban.conf
        │   │   ├── network-ulogd2.conf
        │   │   ├── network-unbound.conf
        │   │   └── network.conf
        │   ├── patterndb.xml
        │   └── syslog-ng.conf
        └── unbound
            └── unbound.conf
```

Further information could be found in the website referred in repo details.

