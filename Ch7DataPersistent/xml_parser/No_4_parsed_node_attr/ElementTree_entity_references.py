"""
XML entity references embedded in the document are converted to the appropriate characters
before values are returned.
"""

from xml.etree import ElementTree

with open('../data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find("entity_expansion")
print(node.tag)
print("     in attribute:", node.attrib["attribute"])
print("     in text     :", node.text.strip())

"""
The automatic conversion means the implementation detail of representing certain characters
in an XML document can be ignored.
"""