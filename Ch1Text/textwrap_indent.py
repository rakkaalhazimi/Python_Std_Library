import textwrap
from DougHellman.Ch1Text.textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += "\n\nSecondParagraph after a blank line."
final = textwrap.indent(wrapped, ">")

print("Quoted block:\n")
print(final)