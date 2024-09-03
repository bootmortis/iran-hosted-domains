# [Iran Hosted Domains](https://github.com/bootmortis/iran-hosted-domains)

Please **use the left sidebar** to navigate through the documentation and find the client you are using.

You can download the domains list from the [release page](https://github.com/bootmortis/iran-hosted-domains/releases/latest).  
For quick review of all release files see [Files section](https://github.com/bootmortis/iran-hosted-domains?tab=readme-ov-file#files).

## General Rules

`iran.dat` can be used in v2fly, v2ray, and xray clients. Similarly, cores related to SingBox can use the `iran-geosite.db` file.

1. Download `iran.dat` file from [here](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat).
2. Copy/Import the file to your client.
   For example:

    - v2ray macOS: `/usr/local/share/v2ray`

3. Add proper rules:

    - `ext:iran.dat:all` in bypass section
    - `ext:iran.dat:ads` in block section

4. Reconnect.

?> In v2ray/Xray clients you can set Domain Resolution Strategy to `IPIfNonMatch` for better routing, or `AsIs` for better performance. See [#83](https://github.com/bootmortis/iran-hosted-domains/issues/83) for more info.

### Full categories

-   `all`: a combination of `other` and `tld-ir`, should be used as `direct`.
-   `ads`: Iran-related advertising services that need to be `blocked`.
-   `proxy`: Iran-related domains that are blocked inside of iran and need to be `proxied`.
-   `ir`: handpicked `.ir` domains, use as `direct`.
-   `other`: non `.ir` domains, use as `direct`.
-   `tld-ir`: all `.ir` domains, use as `direct`.
