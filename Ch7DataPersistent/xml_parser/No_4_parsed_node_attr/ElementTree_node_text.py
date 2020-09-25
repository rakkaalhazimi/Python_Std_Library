"""
The text content of the nodes is available, along with the tail text, which comes after the
end of a close tag.
"""

from xml.etree import ElementTree

with open("../data.xml", "rt") as f:
    tree = ElementTree.parse(f)

for path in ["./child", "./child_with_tail"]:
    node = tree.find(path)
    print("  child node text:", node.text)
    print("  and tail text:", node.tail)

"""
The child node on line 3 contains embedded text, and the node on line 4 has text with a
tail (including whitespace).
"""