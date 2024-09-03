# OpenWrt Pass Wall

این دستورالعمل‌ها برای [کلاینت OpenWrt pass wall](https://github.com/xiaorouji/openwrt-passwall) می‌باشند.

## مسیریابی :id=routing

?> فقط با هسته Xray تست شده است. (با هسته v2ray هم ممکن است کار کند)

1. آخرین نسخه‌ی فایل [iran.dat](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat) را دانلود کنید.

```shell
curl -LO https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat
```

2. فایل `iran.dat` را به دایرکتوری `/usr/share/v2ray/` منتقل کنید. (شما می توانید دایرکتوری صحیح را در `Pass Wall -> Rule Manage -> Location of V2ray/Xray asset`ببینید)

```shell
mv iran.dat /usr/share/v2ray/
```

3. قوانین shunt زیر را در بخش `Pass Wall -> Rule Manage -> Shunt Rules` به همین ترتیب ایجاد کنید:

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

4. یک Node جدید در `Pass Wall -> Node List -> Add` با مشخصات زیر ایجاد کنید:

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

5. به `Pass Wall -> Basic Settings -> Main` بروید و سپس:

<div dir=ltr>

-   TCP Node: `[Shunt]`
-   UDP Node: `Same as the tcp node`

</div>

-   گزینه `Save & Apply` را بزنید.
-   همچنین به تب `DNS` رفته و `Clear IPSET` را بزنید.
