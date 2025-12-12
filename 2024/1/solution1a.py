a = []
b = []
with open('./23/input', 'r') as fd:
	f = fd.read()
	lines = f.split("\n")
	for i in lines:
		if i:
			parts = i.split(" ")
			a.append(parts[0])
			b.append(parts[1])
diff = 0
for i in range(1000):
	if int(a[i]) > int(b[i]):
		d = int(a[i]) - int(b[i])  
	elif int(a[i]) < int(b[i]):
		d = int(b[i]) - int(a[i])  
	else:
		d = 0
	diff += d
	d = 0
print(diff)
