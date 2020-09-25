"""
To print only the groups of names and feed URLs for the podcasts, leave out all of the
data in the header section by iterating over only the outline nodes, and print the text and
xmlUrl attributes by looking up the values in the attrib dictionary.
"""

from xml.etree import ElementTree

with open("../podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.iter("outline"):
    name = node.attrib.get("text")
    url = node.attrib.get("xmlUrl")
    if name and url:
        print("  %s" % name)
        print("    %s" % url)
    else:
        print(name)

"""
The 'outline' argument to iter() means processing is limited to only nodes with the tag
'outline'.
"""