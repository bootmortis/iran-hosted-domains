# Clash

All clash based clients like: [Clash](https://github.com/BackupTime/clash), [Clash for Windows](https://github.com/cfwtf/clash_for_windows), [Clash Verge](https://github.com/zzzgydi/clash-verge), ...

!> **Important Note**: The main clash repository (`Dreamacro/clash`) has been **unexpectedly deleted** and so is no longer maintained. It is **strongly recommended to avoid using it**. Please consider using alternative clients.

## Routing

1. Make sure you are using at least version `2023.04.13` of [Clash Premium](https://github.com/BackupTime/clash/releases/tag/v1.17.0) Core Or `v1.14.4` of [Clash.Meta](https://github.com/MetaCubeX/Clash.Meta) Core. If not, you can use the old version format described in the third step.
2. Open your current profile/config that you use.
3. Add these lines to the file:

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

> :warning: Note: If you are using older versions add these instead :

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

4. Add these lines to `rules:` section

```yaml
- RULE-SET,iran_ads,REJECT
- DOMAIN-SUFFIX,ir,DIRECT
- RULE-SET,iran_other,DIRECT
- GEOIP,IR,DIRECT
```

5. Save the file.
6. Based on the client, you may need to set clash on `Rule` mode.
