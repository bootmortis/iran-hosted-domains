# SagerNet / Matsuri

You can find the SagerNet client [here](https://github.com/SagerNet/SagerNet) and Matsuri client from [here](https://github.com/MatsuriDayo/Matsuri).

!> Please note that both the SagerNet and Matsuri clients are **no longer maintained**. It is recommended to consider alternative options.

## Routing

1. Download the latest version of [iran.dat](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat).
2. Open SagerNet and go to `Route -> Three dots -> Manage Route Assets`.
3. Import the `iran.dat` file.
4. Go to `Route -> Create Route` and add the following rules:
   - Proxy:
      - domain: `ext:iran.dat:proxy`
      - outbound: `Proxy`
   - Block Ads:
     - domain: `geosite:category-ads-all`
     - outbound: `Block`
   - Block Iran Ads:
     - domain: `ext:iran.dat:ads`
     - outbound: `Block`
   - Bypass Iran Domains:
     - domain: `ext:iran.dat:all`
     - outbound: `Bypass`
   - Bypass Iran geoip:
     - ip: `geoip:ir`
     - outbound: `Bypass`
5. Reconnect.

![sagernet](_images/sagernet.png)