"""
The XML attributes of a node are available in the attrib property, which acts like a
dictionary.
"""

from xml.etree import ElementTree

with open("../data.xml", "rt") as f:
    tree = ElementTree.parse(f)

node = tree.find("./with_attributes")
print(node.tag)
for name, value in sorted(node.attrib.items()):
    print(" %-4s = '%s'" % (name, value))

"""
The node on line 5 of the input file has two attributes, name and foo.
"""