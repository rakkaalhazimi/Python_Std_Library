import os, re

compiler = re.compile(r"Py\d\.\d-")


for filename in os.listdir():
    result = compiler.sub("", filename)
    print(result)
    os.renames(filename, result)
