import re

txt = "The rain in Spain"

x = re.findall("e(.*)S", txt)
print(x)
count=(len(x))
print(f"There are {count} match")
