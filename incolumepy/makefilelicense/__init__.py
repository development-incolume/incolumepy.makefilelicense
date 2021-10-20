import toml
from pathlib import Path

# __root__ = Path(__file__).parent.parent.parent
# assert __root__.is_file(), f'{__root__}'


# def update_version():
#     with Path('version.txt').open('w') as f:
#         f.write(
#             f"{toml.load(__root__.joinpath('pyproject.toml'))['tool']['poetry']['version']}\n"
#         )
#
#
# update_version()
# with open('version.txt') as f:
#     __version__ = f.readline().strip()
path = Path(__file__)


if __name__ == '__main__':
    print(list(path.parents))
    print(path.parents[2])
    print(type(path.parents[2]))
    print(path.parents[2].joinpath('incolumepy', 'makefilelicense'))
    assert path.is_file(), f"{path}"
