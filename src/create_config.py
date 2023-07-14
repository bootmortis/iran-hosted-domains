import json
from typing import Iterable

import constants as consts
import utils


def shadowrocket(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
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
        "IP-CIDR,192.168.0.0/16,DIRECT\n"
        "IP-CIDR,10.0.0.0/8,DIRECT\n"
        "IP-CIDR,172.16.0.0/12,DIRECT\n"
        "IP-CIDR,127.0.0.0/8,DIRECT\n"
        "GEOIP,IR,DIRECT\n"
    )
    config += "\n".join(f"DOMAIN-SUFFIX,{domain},REJECT" for domain in ads_domains) + "\n"
    config += "DOMAIN-SUFFIX,ir,DIRECT\n"
    config += "\n".join(f"DOMAIN-SUFFIX,{domain},DIRECT" for domain in bypass_domains) + "\n"
    config += (        

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


def clash(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
    text_config_other = yaml_config_other = text_config_ads = yaml_config_ads = (
        "# Clash\n"
        "# Wiki: https://dreamacro.github.io/clash/premium/rule-providers.html#rule-providers\n"
    )
    
    text_config_other += "".join(f"+.{domain}\n" for domain in bypass_domains)
    yaml_config_other += "payload:\n" + "".join(f"  - '+.{domain}'\n" for domain in bypass_domains)
    text_config_ads += "".join(f"+.{domain}\n" for domain in ads_domains)
    yaml_config_ads += "payload:\n" + "".join(f"  - '+.{domain}'\n" for domain in ads_domains)


    utils.save_to_file(consts.clash_path_text_other, text_config_other)
    utils.save_to_file(consts.clash_path_yaml_other, yaml_config_other)
    utils.save_to_file(consts.clash_path_text_ads, text_config_ads)
    utils.save_to_file(consts.clash_path_yaml_ads, yaml_config_ads)


def surge(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
    ruleset_config_other = ruleset_config_ads =  (
        "# Surge\n"
        "# Manual: https://manual.nssurge.com/rule/ruleset.html\n"
    )
    ruleset_config_other += "".join(f"DOMAIN-SUFFIX,{domain}\n" for domain in bypass_domains)    
    ruleset_config_ads += "".join(f"DOMAIN-SUFFIX,{domain}\n" for domain in ads_domains)        


    domainset_config_other = domainset_config_ads = (
        "# Surge\n"
        "# Manual: https://manual.nssurge.com/rule/domain-based.html\n"
    )    
    domainset_config_other += "".join(f".{domain}\n" for domain in bypass_domains)
    domainset_config_ads += "".join(f".{domain}\n" for domain in ads_domains)           


    utils.save_to_file(consts.surge_ruleset_path_other, ruleset_config_other)
    utils.save_to_file(consts.surge_domainset_path_other, domainset_config_other) 
    utils.save_to_file(consts.surge_ruleset_path_ads, ruleset_config_ads)
    utils.save_to_file(consts.surge_domainset_path_ads, domainset_config_ads)          


def hysteria(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
    acl_client = acl_server =  (
        "# Hysteria\n"
        "# Docs: https://hysteria.network/docs/acl\n"
    )

    acl_client += "".join(f"block domain-suffix {domain}\n" for domain in ads_domains) 
    acl_client +=  (
        "direct domain-suffix ir\n"
        "direct country ir\n"
    )
    acl_client += "".join(f"direct domain-suffix {domain}\n" for domain in bypass_domains) 
    acl_client += "proxy all"


    acl_server +=  (
        "block domain-suffix ir\n"
        "block country ir\n"
    )
    acl_server += "".join(f"block domain-suffix {domain}\n" for domain in ads_domains)
    acl_server += "".join(f"block domain-suffix {domain}\n" for domain in bypass_domains) 
    acl_server += "direct all"              

       
    utils.save_to_file(consts.hysteria_client_path, acl_client)
    utils.save_to_file(consts.hysteria_server_path, acl_server)


def switchy_omega(bypass_domains: Iterable[str]):
    config = "127.0.0.1\n" "::1\n" "localhost\n" "*.ir\n"
    config += "\n".join(f"*{domain}" for domain in bypass_domains)

    utils.save_to_file(consts.switchy_omega_path, config)

def mikrotik(bypass_domains: Iterable[str], ads_domains: Iterable[str]):
    ir_address_list_name = "IRAN-HOSTED-DOMAINS"
    ir_domains_config = (
        f"/log info \"Loading {ir_address_list_name} address list\"\n"
        "/ip firewall address-list remove [/ip firewall address-list find list={ir_address_list_name}]\n"
        "/ip firewall address-list\n"
    )
    ir_domains_config += "\n".join(f":do {{ add address={domain} list={ir_address_list_name} }} on-error={{}}" for domain in bypass_domains)

    ads_address_list_name = "IRAN-ADS-DOMAINS"
    ads_domains_config = (
        f"/log info \"Loading {ads_address_list_name} address list\"\n"
        "/ip firewall address-list remove [/ip firewall address-list find list={ads_address_list_name}]\n"
        "/ip firewall address-list\n"
    )
    ads_domains_config += "\n".join(f":do {{ add address={domain} list={ads_address_list_name} }} on-error={{}}" for domain in ads_domains)

    utils.save_to_file(consts.mikrotik_path_ir, ir_domains_config)
    utils.save_to_file(consts.mikrotik_path_ads, ads_domains_config)
