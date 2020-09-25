"""
Event-style processing is more natural for some operations, such as converting XML
input to some other format. This technique can be used to convert the list of podcasts
from the earlier examples from an XML file to a CSV file, so they can be loaded into a
spreadsheet or database application.
"""

import csv
from xml.etree.ElementTree import iterparse
import sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ""

parsing = iterparse("../podcasts.opml", events=["start"])

for (event, node) in parsing:
    if node.tag != "outline":
        # Ignore anything not part of the outline.
        continue
    if not node.attrib.get("xmlUrl"):
        # Remember the current group.
        group_name = node.attrib["text"]
    else:
        # Output podcast entry.
        writer.writerow(
            (group_name, node.attrib["text"],
            node.attrib["xmlUrl"],
            node.attrib.get("htmlUrl", ""))
        )

"""
This conversion program does not need to hold the entire parsed input file in memory, and
processing each node as it is encountered in the input is more efficient.
"""