from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("Cython_4.pyx"),  # vX indicates different versions
    include_dirs=[numpy.get_include()]
)
