# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-ubigeo-peru',
    version='0.1',
    url='https://github.com/PuercoPop/django-tagging-type',
    license='GPL v.3',
    description='Mi propia ingenieria para tag :/',

    long_description=read('README.md'),

    author='Miguel Angel Cumpa Asuña',
    author_email='themiseck.rock@gmail.com',

    packages=find_packages(),

    install_requires=['setuptools'],

    classifiers=[
        'Development Status :: Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v.3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
