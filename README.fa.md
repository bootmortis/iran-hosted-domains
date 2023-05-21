<div dir=rtl>

#  دامنه‌های میزبانی شده در ایران

- [English Document](README.md)

> 🚨 برای دلایل امنیتی، بهتر است از یک اکانت جداگانه و غیرشخصی برای فعالیت‌های GitHubتان استفاده کنید.
>
> 🚨 قبل از push کردن به GitHub تغییراتتان مطمئن شوید که ایمیل شخصیتان قابل مشاهده نیست. [اطلاعات بیشتر](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address)


بسیاری از سرویس‌ها و دامنه‌های خارج از ایران سانسور و مسدود شده‌اند و باید برای دسترسی به آن‌ها از VPN و Proxy هایی با امنیت بالا استفاده کنیم، جدای از این مسئله دسترسی به بعضی سرویس‌های ایرانی از طریق IP خارجی مسدود شده است. حال برای رد کردن این سرویس ها لیستی از دامنه‌های داخلی را جمع کرده‌ایم تا با اضافه کردن آن‌ به کلاینت‌های مورد استفاده، دیگر نیاز به قطع کردن VPN برای دسترسی به سرویس‌های داخلی نباشد.

## سلب مسئولیت
  این مخزن فهرستی گردآوری شده از منابع عمومی و در دسترس مردم در مورد وب سایت های میزبانی شده در ایران است. این فقط برای مقاصد اطلاعات عمومی در نظر گرفته شده است و برای ارائه راهنمایی در مورد نحوه اتصال یا ایجاد یا مدیریت یک شبکه خصوصی مجازی (VPN) در نظر گرفته **نشده** است. محتوای این مخزن همانطور که هست ارائه شده است و ما هیچ گونه اظهارنظر یا ضمانتی، صریح یا ضمنی، در مورد کامل بودن، دقت، قابلیت اطمینان، مناسب بودن یا در دسترس بودن اطلاعات موجود در این مخزن نداریم. هر گونه اتکای شما به چنین اطلاعاتی کاملاً به عهده شماست. ما مسئولیتی در قبال خطاها یا حذفیات در اطلاعات یا هر گونه ضرر، خسارت یا سایر تعهدات ناشی از استفاده از آن نخواهیم داشت. لطفاً قبل از استفاده از هر گونه اطلاعات این مخزن احتیاط کنید و با یک متخصص واجد شرایط مشورت کنید.
  


## روش استفاده

بسته به اینکه از کدام کلاینت استفاده می‌کنید، ممکن است متفاوت باشد.  لیست دامنه‌ها و فایل‌های مربوط را می‌توانید از [این صفحه][link-release] دریافت کنید.  
برای سیستم routing بهتر در کلاینت‌های v2ray شما می‌توانید پارامتر `Domain Resolution Strategy` را به `IPIfNonMatch` تغییر دهید. [اطلاعات بیشتر](https://www.v2ray.com/en/configuration/routing.html) 


### [Qv2ray](https://github.com/Qv2ray/Qv2ray)

شما می‌توانید فایل qv2ray_schema.json را در [این صفحه][link-release] پیدا کنید.
  
1. فایل را دانلود کنید.
2. در بخش `preferences` بر روی `Advanced Route Settings` کلیک کنید.
3. در پایین صفحه، بر روی `import schema...` کلیک کنید.
4. فایل qv2ray_schema.json دانلود شده را انتخاب کنید.
5. در کادر باز شده بر روی yes کلیک کنید.
6. بر روی OK کلیک کنید.

<table>
  <tr>
    <td> <img width="400" src="assets/qv2ray.png"> </td>
  </tr>
</table>

### .dat file

این فایل در تمامی کلاینت‌های v2ray
  v2fly و xray قابل استفاده است.

1. فایل `iran.dat` را از [این صفحه][link-release] دانلود کنید.
2. فایل را در کلاینت خود کپی و یا وارد کنید.  
  به عنوان مثال:
    - v2ray macOS: `/usr/local/share/v2ray`  
3. قوانین مناسب را اضافه کنید:
    - `ext:iran.dat:ir` در بخش bypass
    - `ext:iran.dat:other` در بخش bypass
    - `ext:iran.dat:ads` در بخش block
4. اتصال خود را قطع و وصل کنید.

<table>
  <tr>
    <td> <img align="right" width="400" src="assets/v2ray.png"> </td>
  </tr>
</table>
  
### [SagerNet](https://github.com/SagerNet/SagerNet) / [Matsuri](https://github.com/MatsuriDayo/Matsuri)

1. فایل `iran.dat` را از [این صفحه][link-release] دانلود کنید.
2. فایل را از طریق `Route -> Three dots -> Manage Route Assets`  به کلاینت اضافه کنید.  
3.  از بخش  `Route -> Create Route` قوانین زیر را اضافه کنید:   
</div>  

- Block Ads:
  - domain: `geosite:category-ads-all`
  - outbound: `Block`
- Block Iran Ads:
  - domain: `ext:iran.dat:ads`
  - outbound: `Block`
- Bypass Iran .ir Domains:
  - domain: `regexp:.+\.ir$`
  - outbound: `Bypass`
- Bypass Iran non .ir Domains:
  - domain: `ext:iran.dat:other`
  - outbound: `Bypass`
- Bypass Iran geoip:
  - ip: `geoip:ir`
  - outbound: `Bypass`

<div dir=rtl>  

> برای مشاهده‌ی اسکرین شات از قوانین بالا [اینجا کلیک کنید](https://imgur.com/a/SEq1Bvg).

4. اتصال خود را قطع و وصل کنید.  

<table>
  <tr>
    <td> <img align="right" src="assets/sagernet.png"> </td>
  </tr>
</table>

  
### [NekoBox](https://github.com/MatsuriDayo/NekoBoxForAndroid)

1. فایل `iran-geosite.db` را از [این صفحه][link-release] دانلود کنید.
2. نام فایل را به `geosite.db` تغییر دهید.
3. فایل را از طریق `Route -> Three dots -> Manage Route Assets`  به کلاینت اضافه کنید.  
4.  از بخش  `Route -> Create Route` قوانین زیر را اضافه کنید:   
</div>  

- Block Iran Ads:
  - domain: `geosite:ads`
  - outbound: `Block`
- Bypass Iran .ir Domains:
  - domain: `domain:.ir`
  - outbound: `Bypass`
- Bypass Iran non .ir Domains:
  - domain: `geosite:other`
  - outbound: `Bypass`
- Bypass Iran geoip:
  - ip: `geoip:ir`
  - outbound: `Bypass`

<div dir=rtl>  

5. اتصال خود را قطع و وصل کنید.
  
  ⚠️ مهم: با اینکار فایل پیش‌فرض geosite با `iran-geosite.db` جایگذاری می‌شود و دسته بندی‌های geosite پیش‌فرض مثل `category-ads-all` قابل استفاده نیستند. با آپدیت کردن `geosite.db` از طریق `Manage Route Assets` می‌توانید دوباره از geosite پیش‌فرض استفاده کنید.
  
  
### [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

1. فایل `shadowrocket.conf` را دانلود کنید.
2. در اپلیکیشن بر روی `Import From Cloud` کلیک کرده و فایل مربوط را اضافه کنید.
3. در نهایت، بر روی `shadowrocket.conf`کلیک کرده و `Use Config` را انتخاب کنید.

<table>
  <tr>
    <td>  <img align="right" height="400" src="assets/shadowrocket1.png"> </td>
    <td>  <img align="right" height="400" src="assets/shadowrocket2.png"> </td>
   </tr>
  </tr>
</table>

### [Clash](https://github.com/Dreamacro/clash) (Like [ClashX](https://github.com/yichengchen/clashX) / [clash_for_windows_pkg](https://github.com/Fndroid/clash_for_windows_pkg) / [Clash Verge](https://github.com/zzzgydi/clash-verge) / ...)

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
⚠️ نکته: اگر از نسخه‌های قدیمی تر Clash Core استفاده می‌کنید بجای خطوط بالا این خطوط را به فایل اضافه کنید:
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

 ### [Surge](https://nssurge.com) / [Surfboard](https://getsurfboard.com)
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
4. قسمت 'Outbound Mode' را روی  'Rule-based' ست کنید.

⚠️ نکته: اگر وبسایت‌های فیلتر شده تو حالت 'Rule-based' کار نمی‌کنن این قانون را قبل از قانون 'FINAL' اضافه کنید.
```INI
DOMAIN-KEYWORD,,YourFinalProxy/ProxyGroup,force-remote-dns
```
> به‌جای YourFinalProxy/ProxyGroup پروکسی/گروه پروکسی خودتان را وارد کنید. 

🚨 از DOMAIN-SET و RULE-SET در  [Loon](https://www.nsloon.com) / [LanceX](https://lancex.org) هم می‌تونید استفاده کنید.

   
### [v2rayNG](https://github.com/2dust/v2rayNG)

📽️ [آموزش ویدیویی](https://imgur.com/8qS5ILD)

1. ابتدا `iran.dat` را از [اینجا][link-release] دانلود کنید.
2. از منو، به قسمت `Geo asset files` بروید، `+` را از بالا فشار دهید و فایل `iran.dat` را انتخاب کنید.
2. از منو، به `Settings` بروید و مطمئن شوید که `Domain Strategy` روی `IpIfNonMatch` تنظیم شده است.
3. به بخش `Custom rules` در `Settings` بروید.
  - در تب `DIRECT URL OR IP`، عبارت `ext:iran.dat:ir,ext:iran.dat:other,geoip:ir` را بنویسید، سپس `🗸` را از بالا فشار دهید.
  - در تب `BLOCKED URL OR IP` عبارت `ext:iran.dat:ads` را بنویسید و دوباره از بالا `🗸` را فشار دهید.
4. دکمه‌ی بازگشت را بزنید و تمام.

  
### [V2Ray Server](https://www.v2ray.com/en/configuration/routing.html)
برای مسدود سازی دامنه‌ها و IP های داخلی در سمت سرور لطفا به [این آموزش][link-v2ray-server-block] مراجعه کنید (همچنین حتما [#58](/../../issues/58) را نیز بررسی کنید).
  
### [Nekoray](https://github.com/MatsuriDayo/nekoray)

1. در ابتدا فایل `domains.txt` را  از [بخش رلیز][link-release] دانلود کنید.
2. سپس nekoray را باز کنید و روی آیکون `program` بالا سمت چپ کلیک کنید
3. سپس به ترتیب روی دکمه `preferences` و `routing setting`  کلیک کنید
4. فایل دانلود شده را بر روی قسمت Direct-Domain جایگذاری کنید.
5. سپس بر روی OK کلیک کنید و برنامه را دوباره اجرا کنید.

<table>
  <tr>
    <td> <img align="right" width="400" src="assets/nekoray1.png"> </td>
    <td> <img align="right" width="400" src="assets/nekoray2.png"> </td>
   </tr>
  </tr>
</table>

  
### [v2rayN](https://github.com/2dust/v2rayN)

1. ابتدا فایل `iran.dat` را از [این صفحه][link-release] دانلود کنید و در محل نصب برنامه `v2rayN` در پوشه `bin` قرار دهید.
2. سپس `v2rayN` را باز کنید و روی `Setting` کلیک کنید و گزینه `RoutingSetting` را انتخاب کنید.
3. سپس در پنجره جدید روِی `Advance Function` کلیک کنید و گزینه `Add` را انتخاب کنید.
4. در پنجره جدید در قسمت `Remarks` یک نام انتخاب کنید و در قسمت `Rule List` در قسمت خالی راست کلیک کرده و گزینه `Rule Add` را انتخاب کنید.
5. در پنجره جدید در قسمت `OutboundTag` گزینه `Direct` را انتخاب کنید و سپس در قسمت `Domains` عبارت `ext:iran.dat:ir,ext:iran.dat:other,regexp:^.+\.ir$` را کپی کنید.
6. بر روی گزینه `Confirm` کلیک کنید تا به صفحه اصلی برنامه برگردید.
7. مطمن شوید که از پایین برنامه فسمت `Routing` نام rule انتخابی شما وارد شده است. درغیر اینصورت فلش رو به پایین سمت راست آنرا بزنید و نام rule انتخابی خود را انتخاب کنید.

### [Sing-Box](https://github.com/SagerNet/sing-box)

1. فایل `iran-geosite.db` را از [اینجا][link-release] دانلود کرده و در پوشه sing-box قرار دهید.
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
        "geosite": "ir",
        "outbound": "direct"
      },
      {
        "geosite": "other",
        "outbound": "direct"
      },
      {
        "geosite": "ads",
        "outbound": "block"
      },
      {
        "domain_suffix": [
          ".ir"
        ],
        "outbound": "direct"
      }
    ]
  }
}
```
3. برای اطلاعات بیشتر در مورد قالب کانفیگ sing-box [اینجا را ببینید](https://sing-box.sagernet.org/configuration/).

## به‌روزرسانی فایل `iran.dat` به‌طور خودکار

اطمینان حاصل کردن از داشتن آخرین نسخه فایل `iran.dat` ممکن است برای شما اهمیت داشته باشد. این بخش شما را در راه‌اندازی یک فرآیند خودکار برای به‌روزرسانی فایل راهنمایی خواهد کرد.

### پیش‌نیازها

- باید `curl` و `shasum` را بر روی سیستم خود نصب داشته باشید.

### استفاده

1. اسکریپت [update_iran_dat.sh](scripts/update_iran_dat.sh) را دانلود کنید.
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

اسکریپت `update_iran_dat.sh` فرآیند به‌روزرسانی فایل `iran.dat` را انجام می‌دهد. ابتدا بررسی می‌کند که فایل از قبل وجود دارد و مقدار checksum فایل فعلی را با آخرین نسخه موجود در مخزن مقایسه می‌کند. اگر نسخه جدیدی موجود باشد، فایل جدید را دانلود کرده و جایگزین فایل قبلی می‌کند. اگر فایل محلی وجود نداشته باشد، به سادگی آخرین نسخه را دانلود کرده و در مسیر مشخص شده ذخیره می کند.

**توجه:** اسکریپت فرض می‌کند که شما دسترسی کافی برای نوشتن در پوشه‌ای که فایل `iran.dat` در آن قرار دارد، دارید. اگر با مشکلی مواجه شدید، اطمینان حاصل کنید که اسکریپت مجوز نوشتن مناسبی دارد یا اسکریپت را به‌صورت مطابق نیاز خود تغییر دهید.

قبل از تنظیم cron job، به صورت دستی اسکریپت را تست کنید و اطمینان حاصل کنید که به درستی اجرا می‌شود.

## ایجاد دستی فایل .dat (آموزش)

### ۱. نصب [golang](https://go.dev/doc/install)

نصب کردن نسخه درست مهم است، همیشه آن را از [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community/blob/master/go.mod) بررسی کنید.

### ۲. ایجاد Clone از [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community)

```bash
git clone https://github.com/v2fly/domain-list-community
```
### ۳. آماده‌سازی دامنه‌ها

شما می‌توانید در یک فایل .dat هر چقدر که می‌خواهید گروه‌های متفاوت داشته باشید. هر کدام از این گروه‌ها می‌توانند در بخش bypass، proxy یا blocked باشند و هر چقدر که می‌خواهید دامنه داشته باشند.

هر گروه یک فایل txt است که دامنه‌ها را شامل می‌شود. برای مثال، شما می‌توانید یک فایل ads.txt داشته باشید که شامل دامنه‌های تبلیغاتی می‌شود.

### ۴. انتقال فایل‌ها به /data

شما وقتی `domain-list-community‍` را Clone می‌کنید، هر چیزی که از قبل آن‌جا بود را هم Clone می‌کنید. از آنجایی که به آنها نیازی ندارید هر چیزی که در پوشه data است را پاک کنید.

حالا شما باید فایل‌های خودتان را به پوشه data کپی کنید. مطمئن شوید که پسوند آن‌ها را حذف می‌کنید. برای مثال فایل `ads.txt` باید بشود `ads‍`.

```bash
cd domain-list-community
rm data/*

cp ~/ads.txt data/ads
```
### ۵. اجرای برنامه

```bash
go run ./ --outputdir=../
```
## فایل‌ها

- **iran.dat:** شامل تمام سایت های هاست شده در ایران و دامنه های تبلیغاتی با فرمت خاص.
- **domains.txt:** شامل تمام سایت های هاست شده در ایران.
- **qv2ray_schema.json:** فایل قابل استفاده در کلاینت [Qv2ray](https://github.com/Qv2ray/Qv2ray).
- **shadowrocket.conf:** فایل قابل استفاده در کلاینت [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118).

## منابع و گرامیداشت

- دامنه‌های ایران:
  - [سازمان فناوری اطلاعات ایران](https://eservices.ito.gov.ir/page/iplist) - [Mirror](https://github.com/bootmortis/ito-gov-mirror)
  - [اینماد](https://enamad.ir/DomainListForMIMT) - [Mirror](https://github.com/bootmortis/enamad-mirror)
  - [سامانه مدیریت اینترنت مشتریان شرکت مخابرات ایران](https://adsl.tci.ir/panel/sites)
  - مخزن [V2fly Domain List Community](https://github.com/v2fly/domain-list-community) (لایسنس MIT)
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
[link-v2ray-server-block]: https://github.com/iranxray/hope/blob/main/routing.md#%D9%85%D8%B3%D8%AF%D9%88%D8%AF%D8%B3%D8%A7%D8%B2%DB%8C-%D8%A7%D8%B2-%D8%B3%D9%85%D8%AA-%D8%B3%D8%B1%D9%88%D8%B1
