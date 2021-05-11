import pathlib
from setuptools import setup

curdir = pathlib.Path(__file__).parent

setup(
    name="couchbase-python-readme",
    version="0.1.0",
    description="Validate the Couchbase Python SDK README",
    long_description=open(str(curdir.joinpath("README.md")), "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thejcfactor/couchbase-python-readme",
    author="thejcfactor",
    author_email="jared.casey@couchbase.com",
    license="Apache License 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["couchbase_readme"],
    install_requires=[],
    entry_points={"console_scripts": ["readme=couchbase_readme.__main__:main"]},
)