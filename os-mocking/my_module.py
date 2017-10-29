import os


DEFAULT_EXTENSION = '.txt'


def my_remove(filename):
    if '.' not in filename:
        filename += DEFAULT_EXTENSION
    try:
        os.remove(filename)
    except OSError:  # can be FileNotFoundError on Python 3
        pass  # silence the exception
