# NekoBox for Android

You can find the NekoBox client for Android [here](https://github.com/MatsuriDayo/NekoBoxForAndroid).

### Routing

1. Go to `Settings -> Route Settings` and change `Rule Assets Provider` to [`Chocolate4U/Iran-sing-box-rules`](https://github.com/Chocolate4U/Iran-sing-box-rules).
2. Go to `Route -> Three dots -> Manage Rute Assets` and then update the rules.
3. Go back to `Route` and make sure these rules are exists and enabled:
    - Block Ads:
        - domain: `geosite:category-ads-all`
        - outbound: `Block`
    - Bypass Iran Domains:
        - domain: `geosite:ir`
        - outbound: `Bypass`
    - Bypass Iran geoip:
        - ip: `geoip:ir`
        - outbound: `Bypass`
4. Reconnect.

![nekobox android](_images/nekobox-android.png)
