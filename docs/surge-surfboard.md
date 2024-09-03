# Surge / Surfboard

You can find surge client for Mac & iOS from [here](https://nssurge.com) and surfboard for Android from [here](https://getsurfboard.com).

## Routing

1. Open your current profile/config that you use.
2. Add these lines to `[Rule]` section

```INI
DOMAIN-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_domainset_ads.txt,REJECT,update-interval=432000
DOMAIN-SUFFIX,ir,DIRECT
DOMAIN-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_domainset_other.txt,DIRECT,update-interval=432000
GEOIP,IR,DIRECT
```

> Surfboard ignore update-interval at this moment, consider updating from Tool>External resources

⚠️ Note: If you are using older Surge versions (before Surge for Mac v3.5.1/Surge for iOS v4.2.2) add these instead:

```INI
RULE-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_ruleset_ads.txt,REJECT,update-interval=432000
DOMAIN-SUFFIX,ir,DIRECT
RULE-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_ruleset_other.txt,DIRECT,update-interval=432000
GEOIP,IR,DIRECT
```

3. Save the file.
4. Set 'Outbound Mode' to 'Rule-based'.

⚠️ Note : in case that blocked websites are not working with 'Rule-based' mode, consider adding this rule before 'FINAL' rule:

```INI
DOMAIN-KEYWORD,,YourFinalProxy/ProxyGroup,force-remote-dns
```

> Use your own Proxy/ProxyGroup instead of 'YourFinalProxy/ProxyGroup'

?> You can also use Surge's Rule-Set or Domain-Set in [Loon](https://www.nsloon.com) / [LanceX](https://lancex.org).
