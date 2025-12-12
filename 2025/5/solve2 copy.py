import os
#593 too low
#598 works
##print("PART TWO")

i = 'input'
i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

empty = lines.index("")

rangesTemp = lines[:empty]
ranges = []
for r in rangesTemp:
    ranges.append([int(r.split("-")[0]),int(r.split("-")[1])])

total = 0
sorted_ranges = sorted(ranges)
global new_ranges
new_ranges = []


def overlap(r):
    print('\n+++++++++++++++++++++++')
    print(f"new list to check: " + str(r))
    print(f"starting new ranges: " + str(new_ranges))

    if len(new_ranges) == 0:
        print("should be only one")
        new_ranges.append(r)
        return
        
    for i in new_ranges:
        in_range_start = i[0]
        in_range_end = i[1]
        new_start = r[0]
        new_end = r[1]
        
        print(f">>>: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")
        

        # new not found
        if new_start > in_range_end:
            print(f"Checking:")
            new_ranges.append(r)   
            print(f"new: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
            return
        
        elif new_end < in_range_start:
            print(f"Checking:")
            new_ranges.append(r)   
            print(f"new: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
            return

        # total inside one of them, ignore
        elif new_start >= in_range_start and new_end <= in_range_end:
            print(f"inside: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
            return

        # starts inside, but goes more so add new end
        elif new_start >= in_range_start and new_end > in_range_end:
            print(f"start inside: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
            location = new_ranges.index(i)
            new_ranges[location] = [new_ranges[location][0], new_end]
            return

        # starts outside, but ends inside, so add new start
        elif new_start < in_range_start and new_end <= in_range_end:
            print(f"start outside: s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
            location = new_ranges.index(i)
            new_ranges[location] = [new_ranges[new_start, location][1]]
            return

        print(f"SHOULD NOT END UP HERE. Ending new ranges: " + str(new_ranges))

for r in sorted_ranges:
    overlap(r)

print("\n\n\nresults:")
for x in new_ranges:
    print(x)
    start = x[0]
    end =   x[1]
    diff = end - start
    total += diff

print(total)

