import os
#593 too low
#598 works
#print("PART TWO")

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

total = 0
sorted_ranges = sorted(ranges)
global new_ranges
new_ranges = []
#####

def overlap(r):
    print('++++++++++++++')
    print(r)
    print('----')

    if len(new_ranges) == 0:
        new_ranges.append(r)

    for i in new_ranges:
        print(f"Checking:")
        print("POSSIBLE: ")
        print(r)
        print(i)
        print("????????")
        in_range_start = i[0]
        in_range_end = i[1]
        new_start = r[0]
        new_end = r[1]
        

        if new_start != in_range_start and new_end != in_range_start:
            print("?here?")
    
            # new not found
            if (new_start < in_range_start and new_end < in_range_start) or (new_start > in_range_end and new_end > in_range_end):
                new_ranges.append(r)   
                print(f"s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     

            # total inside one of them, ignore
            elif new_start > in_range_start and new_end < in_range_end:
                print(f"s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
                print("ignoring")

            # starts inside, but goes more so add new end
            elif new_start >= in_range_start and new_end > in_range_end:
                print("extending list new end")
                print(f"s {new_start} ins {in_range_start} e {new_end} ine {in_range_end}")     
                location = new_ranges.index(i)
                print(location)
                print("to replace: ")
                print(new_ranges[location])
                new_ranges[location] = [new_ranges[location][0], new_end]
                print("after replace: ")
                print(new_ranges[location])
                print("??")

            # starts outside, but ends inside, so add new start
            elif new_start < in_range_start and new_end <= in_range_end:
                print("extending list new start")
                location = new_ranges.index(i)
                print(location)
                print("to replace: ")
                print(new_ranges[location])
                #new_ranges[location] = [new_ranges[location][0], new_end]
                new_ranges[location] = [new_ranges[new_start, location][1]]
                print("after replace: ")
                print(new_ranges[location])

for r in sorted_ranges:
    start = r[0]
    end =   r[1]
    overlap(r)
print("\n\nresults:::::")
for x in new_ranges:
    print(x)
    start = x[0]
    end =   x[1]
    diff = end - start
    total += diff

print(total)

