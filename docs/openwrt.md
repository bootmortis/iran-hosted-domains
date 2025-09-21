# OpenWrt Passwall

These instructions are for [OpenWrt passwall clients](https://github.com/xiaorouji/).

## Routing

?> Only tested with Xray core. (v2ray core may work too)

1. Update the repo and install the package `v2ray-geosite-ir`, This proccess can also be done through Luci web interface.

```shell
opkg update && opkg install v2ray-geosite-ir
```

2. Create these new Shunt Rules in `Pass Wall -> Rule Manage -> Shunt Rules` in this order:
    1. `Block`:
        - Remarks: `Block`
        - Domain: `ext:iran.dat:ads`
    2. `Proxy`:
        - Remarks: `Proxy`
        - Domain: `ext:iran.dat:proxy`
    3. `Direct`:
        - Remarks: `Direct`
        - Domain: `ext:iran.dat:all` (you can use `other`, `ir` or `tld-ir` instead of `all` if you want. For more info see [Full categories](#full-categories))
        - IP: `geoip:ir` (you can also add `geoip:private` too in a new line)
4. [Only passwall1]Create new node in `Passwall -> Node List -> Add`:
    - Node Remarks: `Shunt`
    - Type: `Xray`
    - Protocol: `Shunt`
    - Block: `Blackhole`
    - Proxy: `Default`
    - Direct: `Direct Connection`
    - Default: One of your other nodes
    - Domain Strategy: `AsIs` for better performance or `IPIfNonMatch` for better routing.
5. Go to `Pass Wall -> Basic Settings -> Main` then:
    - TCP Node: `[Shunt]`
    - UDP Node: `Same as the tcp node`
    - Hit `Save & Apply`
    - You can also go to `DNS` tab and hit `Clear IPSET`.
