# v2rayA

قوانین مسیریابی برای [v2rayA](https://github.com/v2rayA/v2rayA).

## مسیریابی :id=routing

1. آخرین نسخه‌ی فایل [iran.dat](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat) را دانلود کنید و آن را در دایرکتوری assets قرار دهید.
2. از قوانین زیر استفاده کنید ([اطلاعات بیشتر](https://v2raya.org/en/docs/manual/routinga/)):

```
default: proxy

domain(ext:"iran.dat:ads")->block
domain(ext:"iran.dat:proxy")->proxy
domain(ext:"iran.dat:all")->direct
ip(geoip:ir)->direct
```
