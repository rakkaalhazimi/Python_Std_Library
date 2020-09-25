import string
import re

class MyTemplate(string.Template):
    delimiter = "{{"
    pattern = r"""
    \{\{(?:
      (?P<escaped>\{\{) |   # Escape sequence of two delimiters
      (?P<named>(?a:[_a-z][_a-z0-9]*))\}\}      |   # delimiter and a Python identifier
      (?P<braced>(?a:[_a-z][_a-z0-9]*))\}\}  |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    """

t = MyTemplate("""
{{{{
{{var}}
""")

print("MATCHES:", t.pattern.findall(t.template))
print("SUBSTITUTE", t.safe_substitute(var="replacement"))