a = []
b = []
with open('input', 'r') as fd:
	f = fd.read()
	lines = f.split("\n")
	for i in lines:
		if i:
			parts = i.split(" ")
			a.append(parts[0])
			b.append(parts[1])
sim = 0
for i in range(1000):
	s = b.count(a[i])
	s = int(a[i]) * s
	sim += s
	s = 0
print(sim)
