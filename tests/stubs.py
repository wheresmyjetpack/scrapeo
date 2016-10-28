class ElementStub(object):

    attrs = {'content': 'val', 'property': 'seo'}
    is_empty_element = False
    text = 'text'

    def get(self, attr):
        return self.attrs.get(attr)
