"""
Parsed XML documents are represented in memory by ElementTree and Element objects
connected in a tree structure based on the way the nodes in the XML document are nested.
Parsing an entire document with parse() returns an ElementTree instance. The tree
knows about all of the data in the input document, and the nodes of the tree can be
searched or manipulated in place. While this flexibility can make working with the parsed
document more convenient, this approach typically takes more memory than an event-based
parsing approach because the entire document must be loaded at one time.
The memory footprint of small, simple documents, such as the following list of podcasts
represented as an OPML outline, is not significant.
"""

from xml.etree import ElementTree

with open("../podcasts.opml", "rt") as f:
    tree = ElementTree.parse(f)

print(tree)

"""
To parse the file, pass an open file handle to parse().

This method will read the data, parse the XML, and return an ElementTree object.
"""