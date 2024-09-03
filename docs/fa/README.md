# [دامنه‌های میزبانی شده در ایران](https://github.com/bootmortis/iran-hosted-domains)

لطفا **از نوار کناری چپ** برای مرور آموزش‌ها و پیدا کردن کلاینتی که استفاده می‌کنید استفاده کنید.

لیست دامنه‌ها و فایل‌های مربوط را می‌توانید از [این صفحه](https://github.com/bootmortis/iran-hosted-domains/releases/latest) دریافت کنید.  
 برای مرور سریع فایل‌های رلیز شده در این مخزن می‌توانید به بخش [فایل‌ها](https://github.com/bootmortis/iran-hosted-domains/blob/main/README.fa.md#%D9%81%D8%A7%DB%8C%D9%84-%D9%87%D8%A7) مراجعه کنید.

## قوانین کلی

فایل `iran.dat` را می توان در کلاینت های v2fly، v2ray و xray استفاده کرد. به طور مشابه، هسته های مربوط به SingBox می‌توانند از فایل `iran-geosite.db` استفاده کنند.

1. فایل `iran.dat` را از [این‌جا](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat) دانلود کنید.
2. فایل را در کلاینت خود کپی و یا وارد کنید.  
   به عنوان مثال:
    - v2ray macOS: `/usr/local/share/v2ray`
3. قوانین مناسب را اضافه کنید:
    - `ext:iran.dat:all` در بخش bypass
    - `ext:iran.dat:ads` در بخش block
4. اتصال خود را قطع و وصل کنید.

?> برای سیستم routing بهتر در کلاینت‌های v2ray/Xray شما می‌توانید پارامتر `Domain Resolution Strategy` را به `IPIfNonMatch` برای مسیریابی بهتر یا `AsIs` برای کارایی بیشتر تغییر دهید. اطلاعات بیشتر را می‌توانید در [#83](https://github.com/bootmortis/iran-hosted-domains/issues/83) مشاهده کنید.

#### دسته بندی کامل

-   دسته بندی `all`: ترکیبی از `other` و `tld-ir`. استفاده به عنوان `direct`.
-   دسته بندی `ads`: خدمات تبلیغاتی مرتبط با ایران که باید `block` شوند.
-   دسته بندی `proxy`: دامنه‌های مرتبط با ایران که در داخل ایران مسدود شده‌اند و باید `proxy` شوند.
-   دسته بندی `ir`: دامنه‌های `.ir` دستچین شده. استفاده به عنوان `direct`.
-   دسته بندی `other`: دامنه‌های غیر `.ir`. استفاده به عنوان `direct`.
-   دسته بندی `tld-ir`: همه دامنه‌های `.ir`. استفاده به عنوان `direct`.
