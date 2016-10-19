"""scrapeo/helpers.py"""

def node_text(element):
    """Return the text attribute of element

    Arguments:
        element -- an object that responds to the attribute text
    """
    return element.text

def pop_kwargs(obj, *args):
    """Return a tuple of values specified by args from calling pop
    on obj
    """
    return (obj.pop(arg, None) for arg in args)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

