from setuptools import find_packages
from distutils.core import setup

setup(
    name = "math_quiz",
    version = "1.0.0",
    author = "Rajesh Kumar",
    py_modules = ['math_quiz'],
    author_email = "developerajesh95@gmail.com",
    url = "https://github.com/developerajesh95/dsss_homework2/",
    entry_points = {
        'console_scripts': [
            'math_quiz = math_quiz:main'
        ]
    },
    packages=["math_quiz"],
    install_requires=[],
)