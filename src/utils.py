import os
import re
import tempfile
import urllib.request
import zipfile

import requests
import tldextract

URL_REGEX = re.compile(
    r"^"
    r"(?:https?://)?"
    # user:pass authentication
    r"(?:\S+(?::\S*)?@)?"
    r"("
    # IP address exclusion
    # private & local networks
    r"(?!(?:10|127)(?:\.\d{1,3}){3})"
    r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
    r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
    # IP address dotted notation octets
    # excludes loopback network 0.0.0.0
    # excludes reserved space >= 224.0.0.0
    # excludes network & broadcast addresses
    # (first & last IP address of each class)
    r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
    r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
    r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
    r"|"
    # host & domain names, may end with dot
    # can be replaced by a shortest alternative
    # r'(?![-_])(?:[-\w\u00a1-\uffff]{0,63}[^-_]\.)+'
    # r'(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)'
    # # domain name
    # r'(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*'
    r"(?:"
    r"(?:"
    r"[a-z0-9\u00a1-\uffff]"
    r"[a-z0-9\u00a1-\uffff_-]{0,62}"
    r")?"
    r"[a-z0-9\u00a1-\uffff]\."
    r")+"
    # TLD identifier name, may end with dot
    r"(?:[a-z\u00a1-\uffff]{2,}\.?)"
    r")"
    # port number (optional)
    r"(?::\d{2,5})?"
    # resource path (optional)
    r"(?:[/?#]\S*)?"
    r"$",
    re.UNICODE | re.IGNORECASE
)

IP_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
)

IR_DOMAIN_REGEX = re.compile(r"\.ir$", re.IGNORECASE)

PERSIAN_CHARS_REGEX = re.compile(
    r"[\u0622\u0627\u0628\u067E\u062A-\u062C\u0686\u062D-\u0632"
    r"\u0698\u0633-\u063A\u0641\u0642\u06A9\u06AF\u0644-\u0648\u06CC\u06F0-\u06F9]"
)


def extract_domain(url: str) -> str:
    matched_domain = URL_REGEX.search(url.strip())
    domain = matched_domain.group(1) if matched_domain is not None else ""

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def is_not_ip(text: str) -> bool:
    return not bool(IP_REGEX.search(text))


def is_ir(text: str) -> bool:
    return bool(IR_DOMAIN_REGEX.search(text))


def is_url(text: str) -> bool:
    return bool(URL_REGEX.search(text))


def convert_utf8(text: str) -> str:
    return text.encode("utf-8", errors="ignore").decode("utf-8")


def filter_persian(text: str):
    return not bool(PERSIAN_CHARS_REGEX.search(text))


def extract_registered_domain(url: str) -> str:
    return tldextract.extract(url).registered_domain


def letter_digit_hyphen(text: str) -> bool:
    # only allows for `a-zA-Z` + `0-9` + `-` + `.`
    # https://github.com/v2fly/v2ray-core/discussions/1275
    # https://www.rfc-editor.org/rfc/rfc952

    return bool(re.search(r"^[a-zA-Z0-9-\.]+$", text))


def download(url: str, path: str, method: str = 'GET', headers: dict = None, payload: str = None):
    if os.path.exists(path):
        return

    resp = requests.request(method, url, allow_redirects=True, verify=False, headers=headers, data=payload)
    resp.raise_for_status()

    with open(path, "wb") as fp:
        fp.write(resp.content)


def save_to_file(path: str, content: str):
    with open(path, "w") as fp:
        fp.write(content)


def fix_requests_ssl():
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass

def get_v2fly_ir_directories(base_dir, dir):
    # recursive function: recursivly get all line start with `include:` to create a list of iran related files with the new files also
    directories = []
    directories.append(dir)
    with open(base_dir + dir) as f:
        for line in f.readlines():
            if line.startswith('include:'):
                file_name = line.split(':')[1].strip()
                directories.extend(get_v2fly_ir_directories(base_dir, file_name))

    return directories

def get_v2fly_non_ir_domains():
    # download https://github.com/v2fly/domain-list-community/archive/refs/heads/master.zip into /tmp
    url = 'https://github.com/v2fly/domain-list-community/archive/refs/heads/master.zip'
    filehandle, _ = urllib.request.urlretrieve(url)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    domains = []
   
    with tempfile.TemporaryDirectory() as tempdir:
        zip_file_object.extractall(tempdir)

        ir_directories = get_v2fly_ir_directories(tempdir + '/domain-list-community-master/data/', 'category-ir') + ['category-ads-ir']

        for filename in os.listdir(tempdir + '/domain-list-community-master/data'):
            if filename.strip() not in ir_directories:
                filepath = tempdir + '/domain-list-community-master/data/' + filename
                with open(filepath) as f:
                    for line in f.readlines():
                        line = re.sub(r'(?m)^\s*#.*\n?', '', line).strip()
                        if line.startswith("full:"):
                            domains.append(line.split(':')[1])
                        elif not line.startswith("include:"):
                            domains.append(line)

    domains = filter(is_not_ip, domains)
    domains = filter(is_url, domains)

    return sorted(domains)
