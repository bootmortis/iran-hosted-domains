# Surge / Surfboard

شما می‌توانید کلاینت surge برای مک و iOS را از [اینجا](https://nssurge.com) و surfboard برای اندروید را از [اینجا](https://getsurfboard.com) پیدا کنید.

# مسیریابی :id=routing

1. صفحه‌ی پروفایل/تنظیمات فعلی خود را که استفاده می‌کنید باز کنید.
2. سپس خط‌های زیر را به بخش قوانین `[Rule]` اضافه کنید:

```INI
DOMAIN-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_domainset_ads.txt,REJECT,update-interval=432000
DOMAIN-SUFFIX,ir,DIRECT
DOMAIN-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_domainset_other.txt,DIRECT,update-interval=432000
GEOIP,IR,DIRECT
```

> سرف برد update-interval را نادیده می‌گیره، بجاش می‌تونید از طریق Tools> External resources لیست دامنه‌ها را آپدیت کنید.

⚠️ نکته: اگر از نسخه‌های قدیمی‌تر از Surge for Mac v3.5.1/Surge for iOS v4.2.2 استفاده می‌کنید به‌جای DOMAIN-SET از RULE-SET استفاده کنید:

```INI
RULE-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_ruleset_ads.txt,REJECT,update-interval=432000
DOMAIN-SUFFIX,ir,DIRECT
RULE-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_ruleset_other.txt,DIRECT,update-interval=432000
GEOIP,IR,DIRECT
```

3. فایل را ذخیره کنید.
4. قسمت 'Outbound Mode' را روی 'Rule-based' ست کنید.

⚠️ نکته: اگر وبسایت‌های فیلتر شده تو حالت 'Rule-based' کار نمی‌کنن این قانون را قبل از قانون 'FINAL' اضافه کنید.

```INI
DOMAIN-KEYWORD,,YourFinalProxy/ProxyGroup,force-remote-dns
```

> به‌جای YourFinalProxy/ProxyGroup پروکسی/گروه پروکسی خودتان را وارد کنید.

?> از DOMAIN-SET و RULE-SET در [Loon](https://www.nsloon.com) / [LanceX](https://lancex.org) هم می‌تونید استفاده کنید.
