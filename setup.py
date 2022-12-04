from distutils.core import setup
from setuptools import find_packages

setup(
    name="snowflake",
    version="1.0.0",
    author="Pratik",
    author_email="pratik.raut@fai.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)
