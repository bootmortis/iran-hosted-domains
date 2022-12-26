import re
from typing import Iterable

import requests

import constants as consts
import utils


def g2b_ito_gov() -> Iterable[str]:
    resp = requests.get(consts.g2b_gov_url)
    resp.raise_for_status()

    domains = resp.text
    domains = domains.splitlines()[1:]
    domains = (domain.split(',')[0] for domain in domains)
    return list(set(domains))


def adsl_tci() -> Iterable[str]:
    with open(consts.adsl_tci_file_path, "r") as file:
        return (line.strip() for line in file.readlines())


def ads() -> Iterable[str]:
    resp = requests.get(consts.ads_url)
    resp.raise_for_status()

    ads = resp.text
    ads = re.sub(r'(?m)^\s*#.*\n?', '', ads)
    ads = ads.splitlines()[1:]
    ads = (ad.strip() for ad in ads if ad.strip() != '')
    ads = filter(utils.is_not_ip, ads)
    ads = filter(utils.is_url, ads)
    return sorted(ads)
