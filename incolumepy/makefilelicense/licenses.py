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
    :param license: [agpl gpl lgpl mit mpl apache bsl unlicense]
    :return: the license of reference
    """
    license = license or 'MIT'
    url = 'https://choosealicense.com/licenses/'

    try:
        req = requests.get(url)
        # print(req.content)
        soup = BeautifulSoup(req.content, 'html.parser')
        query = soup.find('a', href=re.compile(f'/licenses/{license}*', flags=re.I))
        # print(query)
        # print(query.get('href'))

        nurl = urljoin(url, query.get('href'))
        # print(nurl)
        page = requests.get(nurl)
        soup = BeautifulSoup(page.content, 'html.parser')
        q = soup.find('pre', attrs={'id': 'license-text'})
        # print(q.text)
        Path('LICENSE').write_text(q.text)
        return True
    except (AttributeError, requests.RequestException):
        return False


if __name__ == '__main__':
    # licenses('AGPL')
    # print('===')
    # licenses()
    # licenses('apache')
    # licenses('mozilla')
    # licenses('boost')
    # licenses('unlicense')
    print(licenses('gpl'))
