"""
It is possible to take advantage of the fact that the outline nodes are nested only two
levels deep. Changing the search path to .//outline/outline means the loop will process
only the second level of outline nodes.
"""

from xml.etree import ElementTree

with open("../podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

for node in tree.findall(".//outline/outline"):
    url = node.attrib.get("xmlUrl")
    print(url)


"""
All of the outline nodes nested two levels deep in the input are expected to have the xmlURL
attribute referring to the podcast feed, so the loop can skip checking for the attribute before
using it.

This version is limited to the existing structure, though, so if the outline nodes are ever
rearranged into a deeper tree, it will stop working.
"""