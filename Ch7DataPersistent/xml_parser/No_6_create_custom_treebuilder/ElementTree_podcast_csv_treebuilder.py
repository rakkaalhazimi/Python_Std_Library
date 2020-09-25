"""
A potentially more efficient means of handling parse events is to replace the standard tree
builder behavior with a custom version. The XMLParser parser uses a TreeBuilder to process
the XML and call methods on a target class to save the results. The usual output is an
ElementTree instance created by the default TreeBuilder class. Replacing TreeBuilder with
another class allows it to receive the events before the Element nodes are instantiated, saving
that portion of the overhead.
The XML-to-CSV converter from the previous section can be reimplemented as a tree
builder.
"""

import csv
import io
from xml.etree.ElementTree import XMLParser
import sys


class PodcastListToCSV(object):

    def __init__(self, outputFile):
        self.writer = csv.writer(
            outputFile,
            quoting=csv.QUOTE_NONNUMERIC
        )
        self.group_name = ""

    def start(self, tag, attrib):
        if tag != "outline":
            # Ignore anything not part of the outline.
            return
        if not attrib.get("xmlUrl"):
            # Remember the current group.
            self.group_name = attrib["text"]
        else:
            # Output a podcast entry.
            self.writer.writerow(
                (self.group_name,
                 attrib["text"],
                 attrib["xmlUrl"],
                 attrib.get("htmlUrl", ""))
            )

    def end(self, tag):
        """Ignore closing tags"""

    def data(self, data):
        """Ignore data inside nodes"""

    def close(self, data):
        """Nothing special to do here"""


target = PodcastListToCSV(sys.stdout)
parser = XMLParser(target=target)
with open("../podcasts.opml", "rt") as f:
    for line in f:
        parser.feed(line)
parser.close()

"""
PodcastListToCSV implements the TreeBuilder protocol. Each time a new XML tag is
encountered, start() is called with the tag name and attributes. When a closing tag is
seen, end() is called with the name. In between, data() is called when a node has content
(the tree builder is expected to keep up with the “current” node). When all of the input is
processed, close() is called. It can return a value, which will be returned to the user of the
TreeBuilder.
"""
