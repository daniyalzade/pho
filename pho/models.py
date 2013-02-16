import copy
from lxml import etree

class Pho(object):
    def __init__(self, node, *args, **kwargs):
        if(isinstance(node, etree._Element)):
            self._node = node
            # Figure a way of setting html here as well
        else:
            self._node = etree.HTML(node)

    @property
    def html(self):
        return etree.tostring(self._node)

    def find(self, name=None, attrs={}, recursive=True):
        nodes = self.find_all(name, attrs)
        return nodes[0] if nodes else None

    def _get_xpath(self, name, key, value):
        """
        @return: str, kwargs
        """
        if isinstance(value, str):
            return (".//%(name)s[@%(key)s='%(value)s']" % ({
                'name': name,
                'key': key,
                'value': value,
                }), {})
        kwargs = {}
        kwargs['namespaces'] = {"re": "http://exslt.org/regular-expressions"}
        return (".//%(name)s[re:match(@%(key)s, '%(pattern)s')]" % ({
            'name': name,
            'key': key,
            'pattern': value.pattern,
            }), kwargs)

    def find_all(self, name=None, attrs={}, recursive=True):
        if attrs:
            key, value = attrs.items()[0]
            xpath, kwargs = self._get_xpath(name, key, value)
            nodes = self._node.xpath(xpath, **kwargs)
        else:
            nodes = self._node.findall('.//' + name)
        if not recursive:
            nodes = [n for n in nodes if n.getparent() == self._node]
        return [Pho(n) for n in nodes]

    def get(self, key, default=None):
        return self._node.attrib.get(key, default)

    def __getitem__(self, key):
        return self._node.attrib[key]

    def get_text(self):
        text = ''
        for item in self._node.iter():
            to_add = item.text or item.tail
            if to_add:
                text += to_add
        return text

    def __str__(self):
        return etree.tostring(self._node, pretty_print=True)

    def clean_node(self):
        """
        Returns pho that has been cleaned of attributes. Does not modify
        esiting instance.

        @return: Pho 
        """
        pho = Pho(copy.deepcopy(self._node))
        if not pho:
            return None
        for item in pho._node.iter():
            keys = []
            for key in item.attrib:
                keys.append(key)
            for key in keys:
                etree.strip_attributes(item, key)
        return pho
