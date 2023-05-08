import json
from typing import Iterable

import constants as consts
import utils


def shadowrocket(bypass_domains: Iterable[str]):
    config = (
        "#Shadowrocket\n"
        "[General]\n"
        "fallback-dns-server = \n"
        "private-ip-answer = false\n"
        "bypass-system = true\n"
        "skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com\n"
        "tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.18.0.0/15, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32\n"
        "dns-server = 1.1.1.1,8.8.8.8,8.8.4.4\n"
        "dns-fallback-system = false\n"
        "dns-direct-system = false\n"
        "dns-direct-fallback-proxy = true\n"
        "ipv6 = true\n"
        "[Rule]\n"
        "DOMAIN-SET,https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/surge_domainset.txt,DIRECT,update-interval=432000\n"        
        "IP-CIDR,192.168.0.0/16,DIRECT\n"
        "IP-CIDR,10.0.0.0/8,DIRECT\n"
        "IP-CIDR,172.16.0.0/12,DIRECT\n"
        "IP-CIDR,127.0.0.0/8,DIRECT\n"
        "GEOIP,IR,DIRECT\n"
        "FINAL,PROXY\n"
        "[Host]\n"
        "localhost = 127.0.0.1\n"
    )

    utils.save_to_file(consts.shadowrocket_path, config)


def qv2ray(bypass_domains: Iterable[str], proxied_domains: Iterable[str], ads_domains: Iterable[str]):
    schema = {
        "description": "Iran hosted domains",
        "domainStrategy": "AsIs",
        "domains": {
            "direct": ["regexp:^.+\\.ir$"] + list(bypass_domains),
            "proxy": list(proxied_domains),
            "block": ["geosite:category-ads-all"] + list(ads_domains),
        },
        "ips": {"direct": ["geoip:ir"]},
        "name": "ir_hosted",
    }

    utils.save_to_file(consts.qv2ray_schema_path, json.dumps(schema))


def clash(bypass_domains: Iterable[str]):
    config = (
        "# Clash\n"
        "# Wiki: https://github.com/Dreamacro/clash/wiki/premium-core-features#rule-providers\n"
    )
    config += "".join(f"+.{domain}\n" for domain in bypass_domains)


    utils.save_to_file(consts.clash_path, config)


def surge(bypass_domains: Iterable[str]):
    ruleset_config = (
        "# Surge\n"
        "# Manual: https://manual.nssurge.com/rule/ruleset.html\n"
    )
    ruleset_config += "".join(f"DOMAIN-SUFFIX,{domain}\n" for domain in bypass_domains)    


    domainset_config = (
        "# Surge\n"
        "# Manual: https://manual.nssurge.com/rule/domain-based.html\n"
    )    
    domainset_config += "".join(f".{domain}\n" for domain in bypass_domains)    


    utils.save_to_file(consts.surge_ruleset_path, ruleset_config)
    utils.save_to_file(consts.surge_domainset_path, domainset_config)    


def switchy_omega(bypass_domains: Iterable[str]):
    config = "127.0.0.1\n" "::1\n" "localhost\n" "*.ir\n"
    config += "\n".join(f"*{domain}" for domain in bypass_domains)

    utils.save_to_file(consts.switchy_omega_path, config)
