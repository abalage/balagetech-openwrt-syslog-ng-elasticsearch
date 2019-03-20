# balagetech-openwrt-syslog-ng-elasticsearch
Monitoring home network traffic with OpenWRT, Syslog-ng and Elasticsearch

This repo contains:
* A complete configuration for syslog-ng to logging OpenWRT connection tracking events to Elasticsearch by using syslog-ng
  * It enriches logs with GeoIP, Reverse DNS and session lenghth metadata
* A text file describing an explicit mapping for some attributes of the logs.

Warning! For license issues the python parser referenced in the blog post is not included in this repo.

Further information could be found in the website referred in repo details.

###Contents:
```
/
├── LICENSE
├── README.md
├── elastic
│   └── elastic-mapping-for-openwrt.txt     <- data type mappings for indexes
└── etc
    ├── ulogd.conf                          <- ulogd configuration for OpenWRT 18.06.x
    ├── apparmor.d
    │   └── local
    │       └── sbin.syslog-ng              <- workaround for GitHub issue https://github.com/balabit/syslog-ng/issues/2625
    └── syslog-ng
        └── conf.d
            ├── common.conf
            └── network.conf
```
