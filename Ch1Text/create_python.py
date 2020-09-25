
filled = """import os

print(os.getcwd())
"""

with open("current_file.py", "w") as file:
    file.write(filled)