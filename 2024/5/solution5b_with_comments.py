filename = 'test'
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
				# if both parts are in p
				if r1 in p and r2 in p:
					if p.index(r1) < p.index(r2):
						#print(r)
						#print(r1)
						#print(r2)
						#print(p.index(r1))		
						#print(p.index(r2))		
						#print(p)
						gg.append(True)
					else:
						gg.append(False)

	#if False not in gg:
	if False in gg:
		#number = int(p[int(len(p)/2)])
		#total += number
		bad_lines.append(p)


#print("==========")
#[print(i) for i in bad_lines]
#print("==========")


good_lines = []
for p in bad_lines:
	for x in range(30):
		for i in p: # i = actual data numbers
			for r in rules: # r = rule
				if i in r: 
					rr = r.split("|")
					r1 = rr[0]		
					r2 = rr[1]
					# if both parts are in p
					if r1 in p and r2 in p:
						if p.index(r1) > p.index(r2):
							#print("--------")
							##print(p)
							#print(r)
							#print(r1)
							#print(r2)
							#print(p.index(r1))		
							#print(p.index(r2))		
							p[p.index(r1)] = r2		
							p[p.index(r2)] = r1	
							#print(p)

	#print(p)
	good_lines.append(p)

total = 0
#[print(i) for i in good_lines]
for p in good_lines:
	#p = line.split(",")
	gg = []
	for i in p: # i = actual data numbers
		for r in rules: # r = rule
			if i in r: 
				rr = r.split("|")
				r1 = rr[0]		
				r2 = rr[1]
				# if both parts are in p
				if r1 in p and r2 in p:
					if p.index(r1) < p.index(r2):
						print(p)
						#print(r)
						#print(r1)
						#print(r2)
						#print(p.index(r1))		
						#print(p.index(r2))		
						#print(p)
						gg.append(True)
					else:
						gg.append(False)
						print("BAD")
						print(p)
						print(rr)
						print("zzz")

	if False not in gg:
		number = int(p[int(len(p)/2)])
		total += number

print(total)


