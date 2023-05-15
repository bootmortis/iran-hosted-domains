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

def enamad() -> Iterable[str]:
    resp = requests.get(consts.enamad_url)
    resp.raise_for_status()

    domains = resp.text
    domains = domains.splitlines()[1:]
    domains = (domain.split(',')[2] for domain in domains)
    return list(set(domains))

def adsl_tci() -> Iterable[str]:
    with open(consts.adsl_tci_file_path, "r") as file:
        return (line.strip() for line in file.readlines())


def ads() -> Iterable[str]:
    resp = requests.get(consts.ads_url)
    resp.raise_for_status()

    ads = resp.text
    ads = re.sub(r'(?m)^\s*#.*\n?', '', ads)
    ads = ads.splitlines()
    ads = (ad.strip() for ad in ads if ad.strip() != '')
    ads = filter(utils.is_not_ip, ads)
    ads = filter(utils.is_url, ads)
    ads = filter(utils.letter_digit_hyphen, ads)
    return sorted(ads)

def v2fly(filename = "category-ir") -> Iterable[str]:
    resp = requests.get(consts.v2fly_base_url + filename)
    resp.raise_for_status()

    domains = []
    for line in resp.text.splitlines():
        line = re.sub(r'(?m)^\s*#.*\n?', '', line)
        if line.startswith("include:"):
            domains.extend(v2fly(line.split(":")[1]))
        else:
            domains.append(line)
    
    domains = (domain.strip() for domain in domains if domain.strip() != '')
    domains = filter(utils.is_not_ip, domains)
    domains = filter(utils.is_url, domains)
    return sorted(domains)
