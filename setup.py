#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from setuptools import setup


setup(
    name="manageiq-graphql-client-python",
    use_scm_version=True,
    author="Jillian Tullo",
    author_email="jtullo@redhat.com",
    description="Python client for the ManageIQ GraphQL API",
    license="GPLv2",
    keywords=['api', 'graphql', 'client', 'manageiq'],
    url="https://github.com/jntullo/manageiq-graphql-client-python",
    packages=["manageiq_graphql_client"],
    package_dir={'': 'src'},
    install_requires=[
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers"
    ]
)
