from setuptools import find_packages
from distutils.core import setup

setup(
    name = "math_quiz",
    version = "1.0.0",
    py_modules = ['math_quiz'],
    entry_points = {
        'console_scripts':[
            'math_quiz = math_quiz:main'
        ]
    },
    install_requires=[],
    author = "Rajesh Kumar",
    author_email = "developerajesh95@gmail.com",
    packages = find_packages(),
    install_requires = ["numpy"]
)