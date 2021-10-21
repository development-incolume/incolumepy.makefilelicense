#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from functools import partial
from pathlib import Path
import re


def licenses(license: str = '') -> bool:
    """
    Got license text
    :param license: [agpl gpl lgpl mit mpl bsl apache unlicense] default=mit
    :return: A file named LICENSE with the license of reference
    """
    license = license.casefold() or 'mit'
    repo = Path(__file__).parents[0].joinpath('licenses')

    try:
        license_file = repo.joinpath(f"{license}.txt")
        print(license_file)
        Path('LICENSE').write_text(license_file.read_text())
        # print(license_file)
        return True
    except (AttributeError, ):
        return False


license_agpl = partial(licenses, 'agpl')
license_apache = partial(licenses, 'apache')
license_bsl = partial(licenses, 'bsl')
license_gpl = partial(licenses, 'gpl')
license_lgpl = partial(licenses, 'lgpl')
license_mit = partial(licenses, 'MIT')
license_mpl = partial(licenses, 'mpl')
unlicense = partial(licenses, 'unlicense')

if __name__ == '__main__':
    print(licenses('mpl'))
