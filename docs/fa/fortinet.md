# فورتی نت

یک منبع خارجی نام دامنه، فهرستی پویا است که شامل دامنه‌ها می‌شود و به صورت دوره‌ای از یک سرور خارجی به‌روزرسانی می‌شود. این فهرست در قالب یک فایل متنی در یک سرور خارجی ذخیره می‌شود.

کانکتور منبع خارجی نام دامنه را می‌توان در FortiManager ایجاد کرد و هنگامی که از سیاست فایروال با فیلتر DNS استفاده می‌شود، به FortiGate ارسال می‌شود.

# مسیریابی :id=routing

1. به Security Fabric -> External Connectors بروید و Create New را انتخاب کنید. ویزارد Create New Fabric Connector نمایش داده می‌شود.
2. در قسمت External Feeds، نام دامنه را انتخاب کرده و Next را بزنید.
3. نام: یک Domain Name external connector با نام 'Iran Advertising URLs' به همراه لیست URLهایی که باید در فیلتر DNS مسدود شوند، ایجاد کنید.
4. URL منبع خارجی:

```INI
https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/fortinet_domainset_ads.txt
```

5. نرخ به‌روزرسانی: از '100800' استفاده کنید زیرا دامنه‌های میزبانی‌شده در ایران به‌صورت هفتگی به‌روزرسانی دریافت می‌کنند.

![fortinet external](../_images/fortinet-external.png)

4. شما می‌توانید یک فیلتر DNS جدید ایجاد کنید یا قوانین پیش‌فرض را ویرایش کنید؛ در این حالت، ما قوانین پیش‌فرض را تغییر خواهیم داد.

![fortinet default dns](../_images/fortinet-default-dns.png)

5. برای مسدود کردن تبلیغات از طریق FortiGate، گزینه 'Iran Advertising URLs' را روی «هدایت به پورتال مسدودسازی» تنظیم کنید.

![fortinet block ads](../_images/fortinet-block-ads.png)

به خاطر داشته باشید که با این روش، شما تبلیغات را مسدود می‌کنید در حالی که همه سایت‌های دیگر مجاز باقی می‌مانند (مشروط بر اینکه هیچ فیلتر DNS دیگری تنظیم نکرده باشید). با این حال، با استفاده از 'fortinet_domainset_other.txt' و اضافه کردن آن به عنوان یک رابط خارجی دیگر، می‌توانید همه وب‌سایت‌های ایرانی دیگر را مطابق نیاز خود مدیریت کنید.