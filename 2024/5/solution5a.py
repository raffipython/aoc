filename = 'test'
filename = 'input'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
x = lines.index("")
rules = lines[:x]
data = lines[x+1:]

total = 0

for line in data:
	p = line.split(",")
	gg = []
	for i in p:
		for r in rules:
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


