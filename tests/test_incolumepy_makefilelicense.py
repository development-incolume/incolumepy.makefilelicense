from incolumepy.makefilelicense import __version__
from incolumepy.makefilelicense.licenses import licenses
import re
from pathlib import Path
import pytest


def test_version():
    assert re.fullmatch(r'\d(.\d){2}(-\w+.\d+)?', __version__, flags=re.I)


@pytest.mark.parametrize(
    'license, title',
    [
        ('gpl', r'GNU GENERAL PUBLIC LICENSE'),
        ('agpl', r'GNU AFFERO GENERAL PUBLIC LICENSE'),
        ('lgpl', r'GNU LESSER GENERAL PUBLIC LICENSE'),
        ('mit', r'MIT License'),
        ('mpl', r'Mozilla Public License Version 2.0'),
        ('bsl', r'Boost Software License - Version 1.0 - August 17th, 2003'),
        ('apache', r'Apache License'),
        ('unlicense', r'This is free and unencumbered software released into the public domain.'),
    ]
)
def test_licenses(license, title):
    assert licenses(license)
    file = Path('LICENSE')
    with open('LICENSE') as f:
        assert re.match(title, f.readline().strip())
    file.unlink(missing_ok=True)
