# Sing-Box

These are the instructions for [sing-box](https://github.com/SagerNet/sing-box) core configs.

## Routing


### `geosite.srs` formatting:

Open the sing-box config file and edit the Route section in this [format](https://sing-box.sagernet.org/configuration/rule-set/):

```json
{
    "route": {
        "rule_set": [
            {
                "tag": "iran-geosite-ads",
                "type": "remote",
                "format": "binary",
                "update_interval": "7d",
                "url": "https://github.com/bootmortis/sing-geosite/releases/latest/download/geosite-ads.srs"
            },
            {
                "tag": "iran-geosite-all",
                "type": "remote",
                "format": "binary",
                "update_interval": "7d",
                "url": "https://github.com/bootmortis/sing-geosite/releases/latest/download/geosite-all.srs"
            }
        ],
        "rules": [
            {
                "rule_set": ["iran-geosite-ads"],
                "outbound": "block"
            },
            {
                "rule_set": ["iran-geosite-all"],
                "outbound": "direct"
            }
        ]
    }
}
```

?> The sing-box srs files can be found in [our sing-geosite repository](https://github.com/bootmortis/sing-geosite) release section.

#### `geosite.db` formatting:

!> **Important**: Geosite is deprecated and may be removed in the future, check [Migration](https://sing-box.sagernet.org/migration/#migrate-geosite-to-rule-sets) or [here](https://github.com/bootmortis/iran-hosted-domains/issues/180).

1. Download the latest version of `iran-geosite.db` file from [here](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran-geosite.db) and place it in the sing-box working directory.
2. Open the sing-box config file and edit the Route section in this [format](https://sing-box.sagernet.org/configuration/route/geosite/)

```json
{
    "route": {
        "geosite": {
            "path": "iran-geosite.db",
            "download_url": "https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran-geosite.db"
        },
        "rules": [
            {
                "geosite": "all",
                "outbound": "direct"
            },
            {
                "geosite": "ads",
                "outbound": "block"
            },
            {
                "domain_suffix": [".ir"],
                "outbound": "direct"
            }
        ]
    }
}
```

?> For more information about the sing-box config template [see here](https://sing-box.sagernet.org/configuration/).
