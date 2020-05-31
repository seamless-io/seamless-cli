from setuptools import setup, find_packages

from core.constants import PACKAGE_NAME

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click~=7.1.2",],
    entry_points="""
        [console_scripts]
        seamless=core.seamless:cli
    """,
)
