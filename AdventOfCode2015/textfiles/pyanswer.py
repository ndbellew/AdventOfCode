import sys
import re

strings = []
with open("problem5.txt", "r") as file:
    strings = [x.strip() for x in file.readlines()]

# Part 2

x = [s for s in strings if (re.search(r'(..).*\1', s) and re.search(r'(.).\1', s))]
for i in x:
	print(i)

print(len(x))