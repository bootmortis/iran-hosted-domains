# Sing-Box

این دستورالعمل‌ها برای پیکربندی هسته [sing-box](https://github.com/SagerNet/sing-box) می‌باشند.

## مسیریابی :id=routing

#### فرمت `geosite.srs` :id=geositesrs-formatting

فایل کانفیگ sing-box را باز کنید و بخش Route را در این [فرمت](https://sing-box.sagernet.org/configuration/rule-set/) ویرایش کنید:

```json
{
    "route": {
        "rule_set": [
            {
                "tag": "iran-geosite-ads",
                "type": "remote",
                "format": "binary",
                "update_interval": "7d",
                "url": "https://github.com/bootmortis/sing-geosite/releases/latest/download/geosite-ads.srs"
            },
            {
                "tag": "iran-geosite-all",
                "type": "remote",
                "format": "binary",
                "update_interval": "7d",
                "url": "https://github.com/bootmortis/sing-geosite/releases/latest/download/geosite-all.srs"
            }
        ],
        "rules": [
            {
                "rule_set": ["iran-geosite-ads"],
                "outbound": "block"
            },
            {
                "rule_set": ["iran-geosite-all"],
                "outbound": "direct"
            }
        ]
    }
}
```

?> فایل‌های srs مرتبط با sing-box در بخش انتشار [مخزن sing-geosite ما](https://github.com/bootmortis/sing-geosite) قرار دارند.

#### فرمت `geosite.db` :id=geositedb-formatting

!> **نکته**: این فرمت قدیمی شده و ممکن است در نسخه های آینده پشتیبانی نشود، برای مهاجرت به نسخه‌ی جدید [اینجا](https://sing-box.sagernet.org/migration/#migrate-geosite-to-rule-sets) و برای اطلاعات بیشتر [اینجا](https://github.com/bootmortis/iran-hosted-domains/issues/180) را ببینید.

1. آخرین نسخه‌ی فایل `iran-geosite.db` را از [اینجا](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran-geosite.db) دانلود کرده و در پوشه sing-box قرار دهید.
2. فایل کانفیگ sing-box را باز کنید و بخش Route را در این [فرمت](https://sing-box.sagernet.org/configuration/route/geosite/) ویرایش کنید:

```json
{
    "route": {
        "geosite": {
            "path": "iran-geosite.db",
            "download_url": "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran-geosite.db"
        },
        "rules": [
            {
                "geosite": "all",
                "outbound": "direct"
            },
            {
                "geosite": "ads",
                "outbound": "block"
            },
            {
                "domain_suffix": [".ir"],
                "outbound": "direct"
            }
        ]
    }
}
```

?> برای اطلاعات بیشتر در مورد قالب کانفیگ sing-box [اینجا را ببینید](https://sing-box.sagernet.org/configuration/).
