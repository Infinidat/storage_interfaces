import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "storage_interfaces", "__version__.py")) as version_file:
    exec(version_file.read()) # pylint: disable=W0122

_INSTALL_REQUIERS = []

setup(name="storage_interfaces",
      classifiers = [
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          ],
      description="Abstract classes for representing storage-related objects",
      license="BSD3",
      author="Infinidat Ltd.",
      author_email="info@infinidat.com",
      version=__version__, # pylint: disable=E0602
      packages=find_packages(exclude=["tests"]),

      url="https://github.com/Infinidat/storage_interfaces",

      install_requires=_INSTALL_REQUIERS,
      scripts=[],
      namespace_packages=[]
      )