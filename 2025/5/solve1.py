import os
#593 too low

i = 'input'
#i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

empty = lines.index("")

rangesTemp = lines[:empty]
ranges = []
for r in rangesTemp:
    ranges.append([int(r.split("-")[0]),int(r.split("-")[1])])

#items = lines[empty+1:]
ranges = sorted(ranges)
total = []


########################
i = 0
for r in ranges:
    #print("=============")
    print(f"{r[0]} {r[1]}")
    start = r[0]
    end =   r[1]
    #size = len(str(start))
    diff = end - start
    #print(start)
    #print(end)
    #print(diff)
    #[total.append(x) for x in range(start, end+1)]
    #print(f"end of this:    {end}")
    #print(f"start of next:  {ranges[i+1][0]}")
    #print(ranges[i+1][0] - end)
    i += 1


#print(set(total))
print("\n\nFINAL+++++++++")
print(len(set(total)))