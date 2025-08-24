import re

text = 'awijdo woijfeod nvdf 22'
pattern = 'awijdo'
match = re.search(pattern, text)
print(match.group())