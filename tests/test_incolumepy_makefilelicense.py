from incolumepy.makefilelicense import __version__
import re


def test_version():
    assert re.fullmatch(r'\d(.\d){2}(-\w+.\d+)?', __version__, flags=re.I)
