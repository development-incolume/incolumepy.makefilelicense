from incolumepy.makefilelicense import __version__, __root__
from incolumepy.makefilelicense.licenses import (
    license_agpl,
    license_apache,
    license_bsl,
    license_cc0,
    license_gpl,
    license_lgpl,
    license_mit,
    license_mpl,
    licenses,
    unlicense,
)
from incolumepy.makefilelicense.exceptions import LicenseUnavailable
import re
from pathlib import Path
import pytest
from typing import Callable


def test_version():
    assert re.fullmatch(r"\d+(.\d+){2}(-\w+.\d+)?", __version__, flags=re.I)


def test_file_version():
    file = __root__.joinpath("version.txt")
    assert file.is_file(), f"{file}"


def test_file_version_content():
    file = __root__.joinpath("version.txt")
    assert __version__ == file.read_text().strip()


@pytest.mark.parametrize(
    "license, title",
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
    ],
)
def test_licenses(license, title, outputfile):
    assert licenses(license, outputfile)
    file = Path(outputfile)

    with file.open() as f:
        assert re.fullmatch(title, f.readline().strip())
    # file.unlink(missing_ok=True)


@pytest.mark.parametrize("license", ["qgpl", "xpto"])
def test_licenses_raises(outputfile, license):
    # file = Path(outputfile)
    with pytest.raises(LicenseUnavailable):
        licenses(license, outputfile)
    # file.unlink(missing_ok=True)


@pytest.mark.parametrize(
    "func",
    [
        license_agpl,
        license_apache,
        license_bsl,
        license_cc0,
        license_gpl,
        license_lgpl,
        license_mit,
        license_mpl,
        unlicense,
    ],
)
def test_licenses_call(func):
    """
    valid if func is a method
    :param func:
    :return:
    """
    assert isinstance(func, Callable)
    # assert func.__call__()


@pytest.mark.parametrize(
    "func, title",
    [
        (license_agpl, r"GNU AFFERO GENERAL PUBLIC LICENSE"),
        (license_apache, r"Apache License"),
        (license_bsl, r"Boost Software License - Version 1.0 - August 17th, 2003"),
        (license_cc0, "Creative Commons Legal Code"),
        (license_gpl, r"GNU GENERAL PUBLIC LICENSE"),
        (license_lgpl, r"GNU LESSER GENERAL PUBLIC LICENSE"),
        (license_mit, r"MIT License"),
        (license_mpl, r"Mozilla Public License Version 2.0"),
        (
            unlicense,
            r"This is free and unencumbered software released into the public domain.",
        ),
    ],
)
def test_licenses_methods_calls(func, title, outputfile):
    func(outputfile)
    file = Path(outputfile)
    with file.open() as f:
        assert f.readline().strip() == title


def test_asdf(license_type):
    print(license_type)
