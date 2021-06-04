import re

text = "apple price is $99,orange price is $10"
ret = re.search(r".*(\$\d+).*(\$\d+)", text)
print(ret.group())   # apple price is $99,orange price is $10
print(ret.group(0))  # apple price is $99,orange price is $10
print(ret.group(1))  # $99
print(ret.group(2))  # $10
print(ret.groups())  # ('$99', '$10')

