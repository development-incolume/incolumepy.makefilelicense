#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from collections import namedtuple
from tempfile import NamedTemporaryFile

import pytest

License = namedtuple("License", "type title")
list_licenses = [
    ("agpl", "GNU AFFERO GENERAL PUBLIC LICENSE"),
    ("apache", "Apache License"),
    ("bsl", "Boost Software License - Version 1.0 - August 17th, 2003"),
    ("cc0", "Creative Commons Legal Code"),
    ("gpl", "GNU GENERAL PUBLIC LICENSE"),
    ("lgpl", "GNU LESSER GENERAL PUBLIC LICENSE"),
    ("mit", "MIT License"),
    ("mpl", "Mozilla Public License Version 2.0"),
    (
        "unlicense",
        "This is free and unencumbered software released into the public domain.",
    ),
]
licenses = [License(a, b) for a, b in list_licenses]


@pytest.fixture()
def outputfile():
    return NamedTemporaryFile(prefix="license-", suffix=".txt").name


# @pytest.fixture
# def cod_title():
#     license = namedtuple(
#         "License",
#         "license, title",
#     )
#
#     result = (
#         license(x, title)
#         for x, title in [
#             ("agpl", r"GNU AFFERO GENERAL PUBLIC LICENSE"),
#             ("apache", r"Apache License"),
#             ("bsl", r"Boost Software License - Version 1.0 - August 17th, 2003"),
#             ("CC0", "Creative Commons Legal Code"),
#             ("cc0", "Creative Commons Legal Code"),
#             ("GPL", r"GNU GENERAL PUBLIC LICENSE"),
#             ("gpl", r"GNU GENERAL PUBLIC LICENSE"),
#             ("lgpl", r"GNU LESSER GENERAL PUBLIC LICENSE"),
#             ("mit", r"MIT License"),
#             ("mpl", r"Mozilla Public License Version 2.0"),
#             (
#                 "UNLICENSE",
#                 r"This is free and unencumbered software released into the public domain.",
#             ),
#             (
#                 "unlicense",
#                 r"This is free and unencumbered software released into the public domain.",
#             ),
#         ]
#     )


@pytest.fixture
def license_type():
    return [a[0] for a in list_licenses]


@pytest.fixture
def license_title():
    return [a[1] for a in list_licenses]


# @pytest.fixture
# def license_method():
#     return (
#         license_agpl,
#         license_apache,
#         license_bsl,
#         license_cc0,
#         license_gpl,
#         license_lgpl,
#         license_mit,
#         license_mpl,
#         unlicense,
#     )


@pytest.fixture(params=["license_type", "license_title", "license_method"])
def dirname(request):
    return request.getfixturevalue(request.param)


# @pytest.fixture(scope="session")
# def db_conn():
#     db = ...
#     url = ...
#     with db.connect(url) as conn:  # connection will be torn down after all tests finish
#         yield conn
