#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import pytest
from tempfile import NamedTemporaryFile
from collections import namedtuple


@pytest.fixture()
def outputfile():
    return NamedTemporaryFile(prefix="license-", suffix=".txt").name

@pytest.fixture
def cod_title():
    license = namedtuple('License', "license, title",)
    
    result = (
        license(x, title) for x, title in
        [
            ("agpl", r"GNU AFFERO GENERAL PUBLIC LICENSE"),
            ("apache", r"Apache License"),
            ("bsl", r"Boost Software License - Version 1.0 - August 17th, 2003"),
            ("CC0", "Creative Commons Legal Code"),
            ("cc0", "Creative Commons Legal Code"),
            ("GPL", r"GNU GENERAL PUBLIC LICENSE"),
            ("gpl", r"GNU GENERAL PUBLIC LICENSE"),
            ("lgpl", r"GNU LESSER GENERAL PUBLIC LICENSE"),
            ("mit", r"MIT License"),
            ("mpl", r"Mozilla Public License Version 2.0"),
            (
                "UNLICENSE",
                r"This is free and unencumbered software released into the public domain.",
            ),
            (
                "unlicense",
                r"This is free and unencumbered software released into the public domain.",
            ),
        ]
    )

    yield license
