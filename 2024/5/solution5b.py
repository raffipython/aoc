filename = 'input'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
x = lines.index("")
rules = lines[:x]
data = lines[x+1:]

total = 0
bad_lines = []

for line in data:
	p = line.split(",")
	gg = []
	for i in p: # i = actual data numbers
		for r in rules: # r = rule
			if i in r: 
				rr = r.split("|")
				r1 = rr[0]		
				r2 = rr[1]
				if r1 in p and r2 in p:
					if p.index(r1) < p.index(r2):
						gg.append(True)
					else:
						gg.append(False)

	if False in gg:
		bad_lines.append(p)

good_lines = []
for p in bad_lines:
	for x in range(30):
		for i in p: # i = actual data numbers
			for r in rules: # r = rule
				if i in r: 
					rr = r.split("|")
					r1 = rr[0]		
					r2 = rr[1]
					if r1 in p and r2 in p:
						if p.index(r1) > p.index(r2):
							p[p.index(r1)] = r2		
							p[p.index(r2)] = r1	

	good_lines.append(p)

total = 0
for p in good_lines:
	gg = []
	for i in p: # i = actual data numbers
		for r in rules: # r = rule
			if i in r: 
				rr = r.split("|")
				r1 = rr[0]		
				r2 = rr[1]
				if r1 in p and r2 in p:
					if p.index(r1) < p.index(r2):
						gg.append(True)
					else:
						gg.append(False)

	if False not in gg:
		number = int(p[int(len(p)/2)])
		total += number
print(total)
