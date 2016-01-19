# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = '0.1'

install_requires = [
    ]

tests_require = [
    ]

setup(name='treegital.password',
      version=version,
      description="Password management utilities By Treegital",
      long_description=open("README.txt").read() + "\n" +
                       open(join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Treegital',
      author='Treegital',
      author_email='sch@treegital.fr',
      url='http://www.treegital.fr',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['treegital'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      entry_points={},
)
