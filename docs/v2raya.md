# v2rayA

Instructions for [v2rayA](https://github.com/v2rayA/v2rayA) routings.

## Routing

1. Download the latest version of [iran.dat](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat) and place it in assets directory.
2. Use the following rules ([More Info](https://v2raya.org/en/docs/manual/routinga/)):

```
default: proxy

domain(ext:"iran.dat:ads")->block
domain(ext:"iran.dat:proxy")->proxy
domain(ext:"iran.dat:all")->direct
ip(geoip:ir)->direct
```
