""" scrapeo/helpers.py """

def node_text(element):
    """ Return the text attribute of element
    Arguments:
        element -- an object that responds to the attribute text

    """
    return element.text

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

