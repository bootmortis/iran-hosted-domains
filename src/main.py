import os
import re
from functools import reduce
from typing import Iterable

import constants as consts
import create_config
import get_domians
import utils
from data.custom_domains import custom_domains


def collect_and_clean_domains(*domain_set: Iterable[Iterable[str]]) -> Iterable[str]:
    domains = reduce(lambda x, y: set(x).union(set(y)), domain_set)
    domains = (domain.lower() for domain in domains)
    domains = filter(utils.is_url, domains)
    domains = map(utils.convert_utf8, domains)
    domains = filter(utils.filter_persian, domains)
    domains = map(utils.extract_registered_domain, domains)
    domains = filter(utils.letter_digit_hyphen, domains)
    domains = filter(lambda x: x != '', domains)
    domains = filter(lambda domain: domain not in custom_domains["remove"], domains)
    for remove_contain in custom_domains["remove_contain"]:
        domains = list(filter(lambda domain: remove_contain not in domain, domains))
    for remove_regex in custom_domains["remove_regex"]:
        domains = list(filter(lambda domain: not re.match(remove_regex, domain), domains))
    domains = domains + custom_domains["direct"]
    return sorted(set(domains))


if __name__ == "__main__":
    utils.fix_requests_ssl()

    # if not os.path.exists("download"):
    #     os.mkdir("download")
    if not os.path.exists("output"):
        os.mkdir("output")

    # load other domains list
    proxy_domains = sorted(custom_domains["proxy"])
    ad_domains = get_domians.ads()

    # Request data from sources and cleanup
    all_domains = collect_and_clean_domains(
        get_domians.g2b_ito_gov(),
        get_domians.enamad(),
        get_domians.iwmf(),
        get_domians.adsl_tci(),
        get_domians.v2fly(),
    )

    # Divide info
    ir_domains = sorted(filter(utils.is_ir, all_domains))
    other_domains = sorted(set(all_domains).difference(ir_domains))

    # Generate output files
    utils.save_to_file(consts.ad_domains_path, "\n".join(ad_domains))
    utils.save_to_file(consts.other_domains_path, "\n".join(other_domains))
    utils.save_to_file(consts.all_domains_path, "\n".join(all_domains))

    create_config.qv2ray(other_domains, proxy_domains, ad_domains)
    create_config.shadowrocket(other_domains, ad_domains)
    create_config.clash(other_domains, ad_domains)
    create_config.surge(other_domains, ad_domains)
    create_config.hysteria(other_domains, ad_domains)    
    create_config.switchy_omega(other_domains)
