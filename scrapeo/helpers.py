"""scrapeo/helpers.py"""

def pop_kwargs(obj, *args, **kwargs):
    """Return a tuple of values specified by args from calling pop
    on obj
    """
    default = kwargs.get('default', None)
    return (obj.pop(arg, default) for arg in args)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

