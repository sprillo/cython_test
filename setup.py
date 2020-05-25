from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'pytest',
  ext_modules = cythonize(["src/*.pyx"], compiler_directives={
      'embedsignature': True,
      'boundscheck' : False,
      'wraparound' : False}),
)
