#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=None):
    if (name is None) or (not name):
        return "Hello, World!"
    else:
        return "Hello, " + name + "!"

