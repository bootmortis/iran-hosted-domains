# Hysteria

Hysteria client can be found [here](https://github.com/apernet/hysteria).

## Routing

1. Download latest version of [hysteria_client.acl](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/hysteria_client.acl) OR [hysteria_server.acl](https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/hysteria_server.acl) based on your usage.
    - hysteria_client.acl: block Iran ADs and bypass other Iran Domains/IPs (for client)
    - hysteria_server.acl: block all Iran Domains/IPs (for server)
2. Add these lines to your conifg:

```json
    "acl": "acl_file_path",
    "mmdb": "GeoLite2-Country.mmdb"
```

> 'acl_file_path': path of downloaded `.acl` file
