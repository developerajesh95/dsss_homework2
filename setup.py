from setuptools import find_packages
from distutils.core import setup

setup(
    name = "MathQuiz",
    version = "1.0.0",
    author = "Rajesh Kumar",
    author_email = "developerajesh95@gmail.com",
    packages = find_packages(),
    install_requires = ["numpy"]
)