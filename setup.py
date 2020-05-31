from setuptools import setup, find_packages

from core.constants import PACKAGE_NAME, PACKAGE_ENTRY_POINT

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click~=7.1.2",],
    entry_points="""
        [console_scripts]
        {entry_point}=core.seamless:cli
    """.format(entry_point=PACKAGE_ENTRY_POINT),
)
