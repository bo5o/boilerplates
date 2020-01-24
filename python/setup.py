from pathlib import Path

from setuptools import find_packages, setup


def get_version(rel_path):
    for line in Path(rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="myapp",
    version=get_version("myapp/__init__.py"),
    description="A small example package",
    packages=find_packages(),
    python_requires=">=3.6",
)
