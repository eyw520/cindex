from setuptools import (
    find_packages,
    setup,
)

setup(
    name="cindex",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": [
            "cindex=cindex.cli:main",
        ],
    },
)
