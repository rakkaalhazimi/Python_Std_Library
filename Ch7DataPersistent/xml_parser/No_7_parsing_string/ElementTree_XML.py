"""
To work with smaller bits of XML text, especially string literals that might be embedded
in the source of a program, use XML() and the string containing the XML to be parsed as
the only argument.
"""

from xml.etree.ElementTree import XML


def show_node(node):
    print(node.tag)
    if node.text is not None and node.text.strip():
        print("     text: '%s'" % node.text)
    if node.tail is not None and node.tail.strip():
        print("     tail: '%s'" % node.tail)
    for name, value in sorted(node.attrib.items()):
        print("      %-4s = '%s'" % (name, value))
    for child in node:
        show_node(child)

parsed = XML("""
<root>
    <group>
        <child id="a">This is child "a".</child>
        <child id="b">This is child "b".</child>
    </group>
    <group>
        <child id="c">This is child "c".</child>
    </group>
</root>
""")

print("parsed =", parsed)

for elem in parsed:
    show_node(elem)

"""
Unlike with parse(), the return value is an Element instance instead of an ElementTree.
An Element supports the iterator protocol directly, so there is no need to call getiterator().
"""