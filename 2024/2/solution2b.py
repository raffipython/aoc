
def subline(parts):
	for part in range(len(parts) - 1):
		diff = abs(int(parts[part+1]) - int(parts[part]))
		if diff < 1 or diff > 3: 
			return 0

	for part in range(1, len(parts) - 1):
		if int(parts[part - 1]) < int(parts[part]): 
			if int(parts[part]) > int(parts[part + 1]):
				return 0

		if int(parts[part - 1]) > int(parts[part]): 
			if int(parts[part]) < int(parts[part + 1]):
				return 0
	return 1



def safeline(line):
	parts = line.split(" ")
	safeDiff = True
	for part in range(len(parts) - 1):
		diff = abs(int(parts[part+1]) - int(parts[part]))
		if diff < 1 or diff > 3: 
			safeDiff = False
			break

	safeOrder = True
	for part in range(1, len(parts) - 1):
		if int(parts[part - 1]) < int(parts[part]): 
			if int(parts[part]) > int(parts[part + 1]):
				safeOrder = False
				break
		if int(parts[part - 1]) > int(parts[part]): 
			if int(parts[part]) < int(parts[part + 1]):
				safeOrder = False
				break



	new_lists = [parts[:i] + parts[i+1:] for i in range(len(parts))]

	if not safeDiff:
		for new_list in new_lists:
			safeDiff = subline(new_list)
			if safeDiff:
				break

	if not safeOrder:
		for new_list in new_lists:
			safeOrder = subline(new_list)
			if safeOrder:
				break
		
	if safeDiff and safeOrder:
		return 1
	return 0


with open('input', 'r') as fd:
	f = fd.read()
	lines = f.split("\n")

safe = 0
for line in lines:
	if line:
		safe += safeline(line)
print(safe)
