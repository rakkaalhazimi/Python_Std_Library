# String iterpolation, is a process substituting values of variables into placeholders in a string.
import string

values = {"var" : "foo", "unvar" : "oof"}

t = string.Template("""
Variable            : $var
Escape              : $$
Variable in Text    : ${unvar}iable
""")
print("TEMPLATE", t.substitute(values))


s = """
Variable : %(var)s
Escape : %%
Variable in text: %(unvar)siable
"""
print('INTERPOLATION:', s % values)


s = """
Variable : {var}
Escape : {{}}
Variable in text: {unvar}iable
"""
print('FORMAT:', s.format(**values))