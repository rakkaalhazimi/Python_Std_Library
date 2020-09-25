"""
The other API for processing XML documents is event based. The parser generates start
events for opening tags and end events for closing tags. Data can be extracted from the
document during the parsing phase by iterating over the event stream, which is convenient
if it is not necessary to manipulate the entire document afterward and there is no need to
hold the entire parsed document in memory.
Events can be one of the following types:

> start A new tag is encountered. The closing angle bracket of the tag is processed, but not
the contents.

> end The closing angle bracket of a closing tag is processed. All of the children were already
processed.

> start-ns Start a namespace declaration.

> end-ns End a namespace declaration.

iterparse() returns an iterable that produces tuples containing the name of the event
and the node triggering the event.
"""

from xml.etree.ElementTree import iterparse

depth = 0
prefix_width = 8
prefix_dots = "." * prefix_width
line_template = "".join([
    "{prefix:<0.{prefix_len}}",
    "{event:<8}",
    "{suffix:<{suffix_len}}",
    "{node.tag:<20}",
    "{node_id}",
    "{depth:>5}"
])

EVENT_NAMES = ["start", "end", "start-ns", "end-ns"]

for (event, node) in iterparse("../podcasts.opml", EVENT_NAMES):
    if event == "end":
        depth -= 1

    prefix_len = depth * 2

    print(line_template.format(
        prefix=prefix_dots,
        prefix_len=prefix_len,
        suffix="",
        suffix_len=(prefix_width - prefix_len),
        node=node,
        node_id=id(node),
        event=event,
        depth=depth
    ))

    if event == "start":
        depth += 1
        # pass

"""
By default, only end events are generated. To see other events, pass the list of desired
event names to iterparse(), as in this example.
"""