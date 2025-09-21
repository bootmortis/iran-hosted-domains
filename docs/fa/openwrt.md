# OpenWrt Passwall

این دستورالعمل‌ها برای [کلاینتهای یک و دو OpenWrt Passwall](https://github.com/xiaorouji/) می‌باشند.

## مسیریابی :id=routing

?> فقط با هسته Xray تست شده است. (با هسته v2ray هم ممکن است کار کند)

۱. رپوی OpenWrt را بروز کرده و بسته v2ray-geosite-ir را نصب کنید.برای نصب این بسته از طریق رابط وب لوسی نیز میتوانید استفاده کنید. 

```shell
opkg update && opkg install v2ray-geosite-ir
```

۲.قوانین shunt زیر را در بخش `Passwall(2) -> Rule Manage -> Shunt Rules` به همین ترتیب ایجاد کنید:
<div dir=ltr>

1.  `Block`:
    -   Remarks: `Block`
    -   Domain: `ext:iran.dat:ads`
2.  `Proxy`:
    -   Remarks: `Proxy`
    -   Domain: `ext:iran.dat:proxy`
3.  `Direct`:
    -   Remarks: `Direct`
    -   Domain: `ext:iran.dat:all`
    -   IP: `geoip:ir`

</div>

۳.(فقط برای پسوال۱)یک Node جدید در `Passwall -> Node List -> Add` با مشخصات زیر ایجاد کنید:

<div dir=ltr>

-   Node Remarks: `Shunt`
-   Type: `Xray`
-   Protocol: `Shunt`
-   Block: `Blackhole`
-   Proxy: `Default`
-   Direct: `Direct Connection`
-   Default: یکی از سرور‌های خود را انتخاب کنید
-   Domain Strategy: `AsIs` برای کارایی بیشتر یا `IPIfNonMatch` برای دقت مسیر یابی بهتر.

</div>

۴. به `Passwall -> Basic Settings -> Main` بروید و سپس:

<div dir=ltr>

-   TCP Node: `[Shunt]`
-   (passwall1 only)UDP Node: `Same as the tcp node`

</div>

-   گزینه `Save & Apply` را بزنید.
-   همچنین به تب `DNS` رفته و `Clear IPSET` را بزنید.
