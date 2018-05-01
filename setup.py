# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.1.0'


setup(
    name='pywe-jssdk',
    version=version,
    keywords='Wechat Weixin JSSDK',
    description='Wechat JSSDK Module for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pywe-jssdk',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pywe_jssdk'],
    py_modules=[],
    install_requires=['pywe_sign', 'pywe_ticket>=1.1.0', 'shortuuid'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
