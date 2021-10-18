#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import bs4
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin
import re
import requests


def licenses(license: str = '') -> bool:
    """
    Got license text
    :param license: [agpl gpl lgpl mit mpl bsl apache unlicense] default=mit
    :return: A file named LICENSE with the license of reference
    """
    license = license or 'MIT'
    url = 'https://choosealicense.com/licenses/'

    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        query = soup.find('a', href=re.compile(f'/licenses/{license}*', flags=re.I))

        nurl = urljoin(url, query.get('href'))
        page = requests.get(nurl)
        soup = BeautifulSoup(page.content, 'html.parser')
        q = soup.find('pre', attrs={'id': 'license-text'})
        Path('LICENSE').write_text(q.text)
        return True
    except (AttributeError, requests.RequestException):
        return False


if __name__ == '__main__':
    licenses('AGPL')
    licenses('gpl')
