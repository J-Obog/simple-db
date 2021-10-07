from setuptools import setup, find_packages

setup(
    name='simple-db',
    version='1.0',
    description='A lightweight, NoSQL database for Python.',
    url='https://github.com/J-Obog/simple-db',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', 'examples'])
)