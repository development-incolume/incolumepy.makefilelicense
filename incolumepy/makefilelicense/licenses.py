#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from pathlib import Path

url = 'https://choosealicense.com/licenses/'

req = requests.get(url)
# print(req.content)
soup = BeautifulSoup(req.content, 'html.parser')
query = soup.find('a', string=re.compile('AGPL'))
# print(query)
# print(query.get('href'))

nurl = urljoin(url, query.get('href'))
# print(nurl)
page = requests.get(nurl)
soup = BeautifulSoup(page.content, 'html.parser')
q = soup.find('pre', attrs={'id': 'license-text'})
print(q.text)
Path('LICENSE').write_text(q.text)
