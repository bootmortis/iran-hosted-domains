# Clash

کلاینت‌های مختلف clash مانند: [Clash](https://github.com/BackupTime/clash), [Clash for Windows](https://github.com/cfwtf/clash_for_windows), [Clash Verge](https://github.com/zzzgydi/clash-verge), ...

!> **توجه مهم**: مخزن اصلی clash (`Dreamacro/clash`) **به طور ناگهانی حذف شده است** و دیگر توسعه داده نمی‌شود. **به شدت توصیه می‌شود از استفاده از آن خودداری کنید**. لطفاً در نظر داشته باشید که از کلاینت‌های جایگزین استفاده کنید.

## Routing

1. مطمئن شوید که حداقل از ورژن `2023.04.13` [Clash Premium](https://github.com/Dreamacro/clash/releases/tag/premium) Core یا ورژن `1.14.4` [Clash.Meta](https://github.com/MetaCubeX/Clash.Meta) Core استفاده می‌کنید. در غیر این صورت از فرمت نسخه‌ی قدیمی که در مرحله‌ی سوم توضیح داده شده‌است استفاده کنید.
2. صفحه‌ی پروفایل/تنظیمات فعلی خود را که استفاده می‌کنید باز کنید.
3. این خطوط را به فایل اضافه کنید:

```yaml
rule-providers:
    iran_other:
        type: http
        format: text
        behavior: domain
        url: "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/clash_rules_other.txt"
        path: ./ruleset/iran_other.txt
        interval: 432000
    iran_ads:
        type: http
        format: text
        behavior: domain
        url: "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/clash_rules_ads.txt"
        path: ./ruleset/iran_ads.txt
        interval: 432000
```

> :warning: نکته: اگر از نسخه‌های قدیمی تر Clash Core استفاده می‌کنید بجای خطوط بالا این خطوط را به فایل اضافه کنید:

```yaml
rule-providers:
    iran_other:
        type: http
        behavior: domain
        url: "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/clash_rules_other.yaml"
        path: ./ruleset/iran_other.yaml
        interval: 432000
    iran_ads:
        type: http
        behavior: domain
        url: "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/clash_rules_ads.yaml"
        path: ./ruleset/iran_ads.yaml
        interval: 432000
```

4. سپس خط‌های زیر را به بخش قوانین `Rules` اضافه کنید:

```yaml
- RULE-SET,iran_ads,REJECT
- DOMAIN-SUFFIX,ir,DIRECT
- RULE-SET,iran_other,DIRECT
- GEOIP,IR,DIRECT
```

5. فایل را ذخیره کنید.
6. بستگی به نوع کلاینت، ممکن است لازم باشد نرم‌افزار را روی حالت `Rule‍` تنظیم کنید.
