"""Exceptions Defined by the Scrapeo Module
========================================

This module is a collection of exceptions raised by instances of the
classes in the scrapeo.core module.
"""

from .helpers import pop_kwargs

class Error(Exception):
    """Base exception class to inherit from.

    Scrapeo's base exception class from which all other exceptions
    defined in its module must inherit from.
    """
    def __init__(self):
        pass


class ElementAttributeError(Error):
    """Raised when an element does not have a specified attribute.

    Args:
        element (obj): the queried element
        attr (str): the missing attribute of the queried element
        message (str): explanation of error
    """
    def __init__(self, element, attr, message):
        self.element = element
        self.attr = attr
        self.message = message


class ElementNotFoundError(Error):
    """Raised when an element is not found in the DOM.

    Args:
        message (str): explanation of error

    Keyword Args:
        search_term (str): name of element searched for
        attrs (dict): element attr-val pairs used in search
        value (str): single value used in search
    """
    def __init__(self, message, search_term='', attrs=None, value=''):
        self.search_term = search_term
        self.attrs = attrs
        self.value = value
        self.message = message

def raise_element_not_found_error(**kwargs):
    """Function for raising ElementNotFoundError.

    Keyword Args:
        search_term (str): name of element searched for
        attrs (dict): element attr-val pairs used in search
        value (str): single value used in search

    Raises:
        ElementNotFoundError
    """
    search_term, attrs, value = pop_kwargs(kwargs, 'search_term',
                                           'attrs', 'value', default='')
    msg = 'Element not found'
    raise ElementNotFoundError(msg, search_term=search_term,
                               attrs=attrs, value=value)

def raise_element_attribute_error(**kwargs):
    """Function for raising ElementAttributeError

    Keyword Args:
        element (obj): the queried element
        attr (str): the missing attribute of the queried element

    Raises:
        ElementAttributeError
    """
    element, attr = pop_kwargs(kwargs, 'element', 'attr')
    msg = 'Element missing attribute "%s"' % attr
    raise ElementAttributeError(element, attr, msg)
