import textwrap
from DougHellman.Ch1Text.textwrap_example import sample_text

shortened = textwrap.shorten(sample_text, 100)
shortened_wrapped = textwrap.fill(shortened, width=70)

print("\nShortened:\n")
print(shortened_wrapped)