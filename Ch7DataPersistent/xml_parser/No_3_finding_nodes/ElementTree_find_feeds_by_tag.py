"""
Walking through the entire tree, searching for relevant nodes, can be error prone. The
previous example had to look at each outline node to determine if it was a group (nodes
with only a text attribute) or a podcast (with both text and xmlUrl). To produce a simple
list of the podcast-feed URLs, without names or groups, the logic could be simplified by
using findall() to look for nodes with more descriptive search characteristics.
As a first pass at converting the first version, an XPath argument can be used to look
for all outline nodes.
"""

from xml.etree import ElementTree

with open("../podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.findall(".//outline"):
    url = node.attrib.get("xmlUrl")
    if url:
        print(url)
    # print(node)

"""
The logic in this version is not substantially different from the version using getiterator().
It still has to check for the presence of the URL, except that it does not print the group
name when the URL is not found.
"""