from incolumepy.makefilelicense import __version__, __root__
from incolumepy.makefilelicense.licenses import licenses
from incolumepy.makefilelicense.exceptions import LicenseUnavailable
import re
from pathlib import Path
import pytest
from tempfile import NamedTemporaryFile


@pytest.fixture()
def outputfile():
    return NamedTemporaryFile(prefix="license-", suffix=".txt").name


def test_version():
    assert re.fullmatch(r"\d(.\d){2}(-\w+.\d+)?", __version__, flags=re.I)


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
    file.unlink(missing_ok=True)


@pytest.mark.parametrize("license", ["qgpl", "xpto"])
def test_licenses_raises(outputfile, license):
    file = Path(outputfile)
    with pytest.raises(LicenseUnavailable):
        licenses(license, outputfile)
    file.unlink(missing_ok=True)
