import re

bold = re.compile(r"\*{2}(.*?)\*{2}")

text = "Make his **bold**. This **too**"

print("Text", text)
print("Bold", bold.sub(r"<b>\1<b>", text, count=1))