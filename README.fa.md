<div dir=rtl>

# دامنه‌های میزبانی شده در ایران

- [English](README.md)

بسیاری از سرویس‌ها و دامنه‌های خارج از ایران سانسور و مسدود شده‌اند و باید برای دسترسی به آن‌ها از VPN و Proxy هایی با امنیت بالا استفاده کنیم، جدای از این مسئله دسترسی به بعضی سرویس‌های ایرانی از طریق IP خارجی مسدود شده است. حال برای رد کردن این سرویس ها لیستی از دامنه‌های داخلی را جمع کرده‌ایم تا با اضافه کردن آن‌ به کلاینت‌های مورد استفاده، دیگر نیاز به قطع کردن VPN برای دسترسی به سرویس‌های داخلی نباشد.

## سلب مسئولیت

این مخزن فهرستی گردآوری شده از منابع عمومی و در دسترس مردم در مورد وب سایت های میزبانی شده در ایران است. این فقط برای مقاصد اطلاعات عمومی در نظر گرفته شده است و برای ارائه راهنمایی در مورد نحوه اتصال یا ایجاد یا مدیریت یک شبکه خصوصی مجازی (VPN) در نظر گرفته **نشده** است. محتوای این مخزن همانطور که هست ارائه شده است و ما هیچ گونه اظهارنظر یا ضمانتی، صریح یا ضمنی، در مورد کامل بودن، دقت، قابلیت اطمینان، مناسب بودن یا در دسترس بودن اطلاعات موجود در این مخزن نداریم. هر گونه اتکای شما به چنین اطلاعاتی کاملاً به عهده شماست. ما مسئولیتی در قبال خطاها یا حذفیات در اطلاعات یا هر گونه ضرر، خسارت یا سایر تعهدات ناشی از استفاده از آن نخواهیم داشت. لطفاً قبل از استفاده از هر گونه اطلاعات این مخزن احتیاط کنید و با یک متخصص واجد شرایط مشورت کنید.

## روش استفاده

بسته به اینکه از کدام کلاینت استفاده می‌کنید، ممکن است متفاوت باشد. لطفا برای اطلاعات بیشتر در مورد هر کلاینت **[این راهنما](https://bootmortis.github.io/iran-hosted-domains/#/fa/) را ببینید**.

## کلاینت‌ها

راهنمای کلاینت‌ها به [https://bootmortis.github.io/iran-hosted-domains](https://bootmortis.github.io/iran-hosted-domains/#/fa/) منتقل شده است. شما می‌توانید راهنماها و دستورالعمل‌های به‌روز و مربوط به کلاینت‌های خود را در آنجا پیدا کنید.

## دسته‌بندی

- دسته بندی `all`: ترکیبی از `other` و `tld-ir`. استفاده به عنوان `direct`.
- دسته بندی `ads`: خدمات تبلیغاتی مرتبط با ایران که باید `block` شوند.
- دسته بندی `proxy`: دامنه‌های مرتبط با ایران که در داخل ایران مسدود شده‌اند و باید `proxy` شوند.
- دسته بندی `ir`: دامنه‌های `.ir` دستچین شده. استفاده به عنوان `direct`.
- دسته بندی `other`: دامنه‌های غیر `.ir`. استفاده به عنوان `direct`.
- دسته بندی `tld-ir`: همه دامنه‌های `.ir`. استفاده به عنوان `direct`.

## فایل ها

شما همیشه می توانید آخرین نسخه این فایل ها را در [صفحه انتشار][link-release] پیدا کنید.  
شما می توانید روی نام برنامه کلیک کنید تا دستورالعمل های استفاده را ببینید.  
همچنین، برای هر فایل، یک فایل `.sha256` وجود دارد که حاوی هش sha256 آن فایل است.

- فایل‌های **clash_rules_ads.txt** و **clash_rules_ads.yaml** و **clash_rules_other.txt** و **clash_rules_other.yaml**: تمام تبلیغات و دامنه‌های غیر ir را برای [clash](https://bootmortis.github.io/iran-hosted-domains/#/fa/clash) در دو فرمت مختلف شامل می شود.
- فایل **domains.txt**: تمام وب سایت های میزبانی شده در ایران را شامل می شود.
- فایل‌های **hysteria_client.acl** و **hysteria_server.acl**: بخش [Hysteria](https://bootmortis.github.io/iran-hosted-domains/#/fa/hysteria) را ببینید.
- فایل **iran-geosite.db**: برای هسته sing-box بخش [Sing-Box](https://bootmortis.github.io/iran-hosted-domains/#/fa/singbox) را ببینید.
- فایل‌های **geosite-*.srs**: برای sing-box ورژن 1.8 به بعد، این فایل‌ها را می‌توانید از [این صفحه](https://github.com/bootmortis/sing-geosite/releases/latest) دریافت کنید.
- فایل **iran.dat**: تمام وب سایت های میزبانی شده در ایران، تبلیغات و دامنه های مرتبط با پروکسی برای v2ray/xray را شامل می شود، برای اطلاعات بیشتر [دسته بندی های کامل](#دستهبندی) را ببینید.
- فایل **qv2ray_schema.json**: سناریوی json قابل وارد کردن که می تواند در [Qv2ray](https://bootmortis.github.io/iran-hosted-domains/#/fa/qv2ray) استفاده شود.
- فایل **shadowrocket.conf:** فایل conf قابل وارد کردن که می تواند در [Shadowrocket](https://bootmortis.github.io/iran-hosted-domains/#/fa/shadowrocket-ios) استفاده شود.
- فایل‌های **surge_domainset_ads.txt**, **surge_domainset_other.txt**, **surge_ruleset_ads.txt** و **surge_ruleset_other.txt**: تمام تبلیغات و وب سایت های غیر ایرانی میزبانی شده در ایران را برای [Surge](https://bootmortis.github.io/iran-hosted-domains/#/fa/surge-surfboard) در دو فرمت مختلف شامل می شود.
- فایل **switchy_omega.sorl**: دامنه ها را برای [SwitchyOmega](https://bootmortis.github.io/iran-hosted-domains/#/fa/switchyomega) شامل می شود.

## منابع و گرامیداشت

- دامنه‌های ایران:
  - [سازمان فناوری اطلاعات ایران](https://eservices.ito.gov.ir/page/iplist) - [Mirror](https://github.com/bootmortis/ito-gov-mirror)
  - [اینماد](https://enamad.ir/DomainListForMIMT) - [Mirror](https://github.com/bootmortis/enamad-mirror)
  - [سامانه مدیریت اینترنت مشتریان شرکت مخابرات ایران](https://adsl.tci.ir/panel/sites)
  - مخزن [V2fly Domain List Community](https://github.com/v2fly/domain-list-community) (لایسنس MIT)
  - [جشنواره وب و موبایل ایران](https://directory.iwmf.ir/) - [Mirror](https://github.com/Chocolate4U/iwmf.ir-Mirror) (لایسنس MIT)
  - [لیست شخصی][link-custom]
- تبلیغات:
  - مخزن [uBOPa - uBO Parsi filter list](https://github.com/nimasaj/uBOPa) (لایسنس MIT)

اگر شما منابع دیگری می‌شناسید، و یا وب‌سایتی پیدا کرده‌اید که اینجا نیست لطفا یک
[issue][link-issues] باز کنید و یا فایل [custom_domains.py][link-custom] را تغییر داده و [PR][link-pr] ایجاد کنید.

## چگونه کار می کند؟

به وسیله‌ی Github Action یک اسکریپت پایتون اجرا شده و از طریق منابع بالا فایل‌های مربوطه در صفحه‌ی رلیز ایجاد می‌شود.

</div>

[link-custom]: src/data/custom_domains.py
[link-pr]: ../../pulls
[link-issues]: ../../issues/new?assignees=&labels=enhancement&template=request-for-domain-addition-removal.md&title=Add%2FRemove+%60example.com%60
[link-release]: ../../releases/latest
