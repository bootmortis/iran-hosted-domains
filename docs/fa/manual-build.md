# ایجاد دستی فایل .dat

۱. نصب [golang](https://go.dev/doc/install)

نصب کردن نسخه درست مهم است، همیشه آن را از [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community/blob/master/go.mod) بررسی کنید.

۲. ایجاد Clone از [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community)

```bash
git clone https://github.com/v2fly/domain-list-community
```

۳. آماده‌سازی دامنه‌ها

شما می‌توانید در یک فایل .dat هر چقدر که می‌خواهید گروه‌های متفاوت داشته باشید. هر کدام از این گروه‌ها می‌توانند در بخش bypass، proxy یا blocked باشند و هر چقدر که می‌خواهید دامنه داشته باشند.

هر گروه یک فایل txt است که دامنه‌ها را شامل می‌شود. برای مثال، شما می‌توانید یک فایل ads.txt داشته باشید که شامل دامنه‌های تبلیغاتی می‌شود.

۴. انتقال فایل‌ها به /data

شما وقتی `domain-list-community‍` را Clone می‌کنید، هر چیزی که از قبل آن‌جا بود را هم Clone می‌کنید. از آنجایی که به آنها نیازی ندارید هر چیزی که در پوشه data است را پاک کنید.

حالا شما باید فایل‌های خودتان را به پوشه data کپی کنید. مطمئن شوید که پسوند آن‌ها را حذف می‌کنید. برای مثال فایل `ads.txt` باید بشود `ads‍`.

```bash
cd domain-list-community
rm data/*

cp ~/ads.txt data/ads
```

۵. اجرای برنامه

```bash
go run ./ --outputdir=../
```
