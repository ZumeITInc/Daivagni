# Importing regular expression
import re
str = "How are you .How is everything"

# using findall functions
matches = re.findall("How",str)
print(matches)


strin = "this is a regular expression"
# using search function
match = re.search('this',strin)
print(type(match))
print(match)

strings = "Iam learing python"
x = re.search("\s",strings)
print("the first white space character is located in positions:",x.start())
