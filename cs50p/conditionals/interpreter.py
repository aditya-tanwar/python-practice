# Need to take a look at this once I read about the import statement

import re

def parse_expression(expr):
    # \d+  → one or more digits
    # [+\-*/] → one operator (+, -, *, /)
    # | means "or"
    parts = re.findall(r'\d+|[+\-*/]', expr)
    return parts

# Example usage:
expr = input("expression : ")
tokens = parse_expression(expr)

x, y, z = tokens  # unpack into three variables

print("x:", x)
print("y:", y)
print("z:", z)