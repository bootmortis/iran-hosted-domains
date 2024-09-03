# Hysteria

کلاينت Hysteria را می‌توانید [اینجا](https://github.com/apernet/hysteria) پیدا کنید.

## مسیریابی :id=routing

1. با توجه به نیازتون [hysteria_client.acl](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/hysteria_client.acl) یا [hysteria_server.acl](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/hysteria_server.acl) را دانلود کنید.

    - hysteria_client.acl: بلاک کردن تبلیغات ایرانی و بای پس کردن دامنه/آیپی‌های ایران (برای کلاینت)
    - hysteria_server.acl: بلاک کردن تمام دامنه/آیپی‌های ایران (برای سرور)

2. این خط‎ ها را به کانفیگ خودتون اضافه کنید:

```json
    "acl": "acl_file_path",
    "mmdb": "GeoLite2-Country.mmdb"
```

> 'acl_file_path': محل فایل
