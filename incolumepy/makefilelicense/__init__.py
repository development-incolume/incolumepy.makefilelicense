import toml
from pathlib import Path

__root__ = Path(__file__).parent.parent.parent
# assert __root__.is_file(), f'{__root__}'


def update_version():
    with Path('version.txt').open('w') as f:
        f.write(
            f"{toml.load(__root__.joinpath('pyproject.toml'))['tool']['poetry']['version']}\n"
        )


update_version()
with open('version.txt') as f:
    __version__ = f.readline().strip()
