from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize('primes.pyx')
)

# cd src\cpython
# python setup_build.py build_ext --inplace