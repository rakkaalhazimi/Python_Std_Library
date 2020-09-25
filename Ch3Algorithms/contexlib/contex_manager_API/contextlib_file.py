"""
A context manager is responsible for a resource within a code block, possibly creating it
when the block is entered and then cleaning it up after the block is exited.
"""

with open("context.txt", "wt") as text:
    text.write("Hey, I'm writing !")
    # File is automatically closed