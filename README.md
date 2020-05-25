# cython_test
My first attempt at cython.

First set up the virtual env:

```
$ virtualenv -p python3 cython_test_env
$ source cython_test_env/bin/activate
$ pip install -r requirements.txt
```

Then run:

```
$ python setup.py build_ext --inplace
```

Finally:

```
$ python -m pytest
```

Example is from:

```
https://pytestguide.readthedocs.io/en/latest/pytestGuide/
```

TODO: pyproject.toml as per https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html ?

TODO: numpy as per https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html ? `You need to add this path only if you use cimport numpy.'
