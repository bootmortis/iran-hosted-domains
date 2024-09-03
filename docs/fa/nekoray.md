# Nekoray / Nekobox (Desktop)

شما می‌توانید نسخه دسکتاپ این برنامه را از [اینجا](https://github.com/MatsuriDayo/nekoray) پیدا کنید.

## مسیریابی :id=routing

نکوری میتواند از هر دو هسته sing-box و Xray استفاده کند. لطفا از قوانین مسیریابی مربوطه بر اساس هسته انتخابی خود در نکوری استفاده کنید.

?> :information_source: میتوانید با رفتن به `Preferences` > `Basic Settings` > `Core` هسته فعلی مورد استفاده خود را ببینید یا تغییر دهید.

### sing-box core

1. آخرین نسخه‌ی [iran-geosite.db](https://github.com/bootmortis/iran-hosted-domains/releases/download/202409020032/iran-geosite.db) را دانلود کنید.
2. آن را به `geosite.db` تغییر نام دهید.
3. فایل `geosite.db` را در پوشه nekoray به `backup-geosite.db` تغییرنام دهید.
4. فایل `geosite.db` دانلودی را به پوشه nkoray انتقال دهید.
5. روی `Preferences` کلیک کنید و سپس `Routing Setting` را انتخاب کنید.
6. به سربرگ `Simple Route` بروید.
7. خطوط زیر را در قسمت های مربوطه کپی کنید:


-   `Direct, IP`

```
geoip:ir
geoip:private
```

-   `Direct, Domain`

```
geosite:all
```


-   `Proxy, Domain`

```
geosite:proxy
```

-   `Block, Domain`

```
geosite:ads
```

8. روی Ok کلیک کنید و برنامه را دوباره اجرا کنید.

!> **مهم**: با اینکار دسته بندی‌های geosite پیش‌فرض مثل `category-ads-all` قابل استفاده نیستند. برای برگشتن به geosite پیشفرض، فایل `geosite.db` فعلی را حذف کرده و `backup-geosite.db` را به `geosite.db` تغییر نام دهید. همچنین می‌توانید از [sing-geosite](https://github.com/SagerNet/sing-geosite/releases) نسخه اصلی `geosite.db` را دانلود کنید.

![nekoray-sing-box.png](../_images/nekoray-sing-box.png)

### Xray core

1. دانلود آخرین نسخه‌ی [iran.dat](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat).
2. فایل `iran.dat` را در پوشه Nekoray کپی کنید.
3. روی `Preferences` کلیک کنید و سپس `Routing Setting` را انتخاب کنید.
4. به سربرگ `Simple Route` بروید.
5. خطوط زیر را در قسمت های مربوطه کپی کنید:

-   `Direct, IP`

```
geoip:ir
geoip:private
```

-   `Direct, Domain`

```
ext:iran.dat:all
```

-   `Proxy, Domain`

```
ext:iran.dat:proxy
```

-   `Block, Domain`

```
ext:iran.dat:ads
geosite:category-ads-all
```

6.  روی Ok کلیک کنید و برنامه را دوباره اجرا کنید.

![nekoray-xray](../_images/nekoray-xray.png)
