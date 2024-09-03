# به‌روزرسانی فایل iran.dat به‌طور خودکار

اطمینان حاصل کردن از داشتن آخرین نسخه فایل `iran.dat` ممکن است برای شما اهمیت داشته باشد. این بخش شما را در راه‌اندازی یک فرآیند خودکار برای به‌روزرسانی فایل راهنمایی خواهد کرد.

اسکریپت فرآیند به‌روزرسانی فایل `iran.dat` را انجام می‌دهد. ابتدا بررسی می‌کند که فایل از قبل وجود دارد و مقدار checksum فایل فعلی را با آخرین نسخه موجود در مخزن مقایسه می‌کند. اگر نسخه جدیدی موجود باشد، فایل جدید را دانلود کرده و جایگزین فایل قبلی می‌کند. اگر فایل محلی وجود نداشته باشد، به سادگی آخرین نسخه را دانلود کرده و در مسیر مشخص شده ذخیره می کند.

?> **توجه:** اسکریپت فرض می‌کند که شما دسترسی کافی برای نوشتن در پوشه‌ای که فایل `iran.dat` در آن قرار دارد، دارید. اگر با مشکلی مواجه شدید، اطمینان حاصل کنید که اسکریپت مجوز نوشتن مناسبی دارد یا اسکریپت را به‌صورت مطابق نیاز خود تغییر دهید.

قبل از تنظیم cron job و SCHTASK، به صورت دستی اسکریپت را تست کنید و اطمینان حاصل کنید که به درستی اجرا می‌شود.

## لینوکس

### پیش‌نیازها

-   باید `curl` و `shasum` را بر روی سیستم خود نصب داشته باشید.

### استفاده

1. اسکریپت [update_iran_dat.sh](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.sh) را دانلود کنید. (اگر از ash استفاده می‌کنید، فایل [update_iran_dat.ash](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.ash) را دانلود کنید.)

```shell
curl -LO https://raw.githubusercontent.com/bootmortis/iran-hosted-domains/main/scripts/update_iran_dat.sh
```

2. با استفاده از دستور زیر اسکریپت را اجرایی کنید:

```shell
chmod +x update_iran_dat.sh
```

3. با اجرای دستور زیر، فایل crontab را باز کنید:

```shell
crontab -e
```

4. در ویرایشگر crontab، خط زیر را اضافه کنید تا اسکریپت هر سه‌شنبه اجرا شود (یک روز پس از به‌روزرسانی فایل `iran.dat`):

```shell
0 0 * * 2 /path/to/update_iran_dat.sh /path/to/iran.dat
```

مطمئن شوید که `/path/to/update_iran_dat.sh` را با مسیر واقعی اسکریپت در سیستم خود و `/path/to/iran.dat` را با مسیر واقعی فایل `iran.dat` که می‌خواهید به‌روزرسانی کنید، جایگزین کرده‌اید.

5. فایل crontab را ذخیره کرده و ویرایشگر را ببندید.

## ویندوز

### پیش‌نیازها

-   به دلیل فاقد امضا بودن فایل اسکریپت، برای اجرای صحیح آن نیاز به تغییر تنظیمات `ExecutionPolicy` می‌باشد.
-   برای این انجام این تغییر، یک پنجره `Powershell` را با دسترسی `Administrator` باز نموده و دستور زیر را در آن اجرا نمایید:

```powershell
Set-ExecutionPolicy unrestricted
```

### استفاده

1. اسکریپت [update_iran_dat.ps1](https://github.com/bootmortis/iran-hosted-domains/blob/main/scripts/update_iran_dat.ps1) را دانلود کنید و آن را در محل مناسبی (مثلا در کنار فایل `iran.dat`) قرار دهید.

2. یک پنجره `cmd` با دسترسی `Administrator` باز کرده و فرمان زیر را در آن اجرا کنید:

```cmd
SCHTASKS /CREATE /SC WEEKLY /D TUE /TN "UPDATE IRAN.DAT" /TR "powershell -File '<path\to\update_iran_dat.ps1>' '<path\to\iran.dat>'" /ST 19:00
```

مطمئن شوید که `<path\to\update_iran_dat.ps1>` را با مسیر واقعی اسکریپت در سیستم خود و `<path\to\iran.dat>` را با مسیر واقعی فایل `iran.dat` که می‌خواهید به‌روزرسانی کنید، جایگزین کرده‌اید.
