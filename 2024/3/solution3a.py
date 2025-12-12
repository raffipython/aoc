import re

def find_matches(line):
	regex = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
	matches = regex.findall(line)
	return matches

def process_match(match):
	a = int(match.split("(")[1].split(",")[0])
	b = int(match.split("(")[1].split(",")[1].split(")")[0])
	return a * b

with open('input', 'r') as fd:
	lines = fd.read().split("\n")

total = 0

for line in lines:
	if line:
		matches = find_matches(line)
		for match in matches:
			total += process_match(match)
print(total)
