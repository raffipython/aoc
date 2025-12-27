import os

i = 'input'
i = 'input2'

with open(i, 'r') as fd:
    f = fd.read()
    lines = f.split('\n')

def next(x):
    max = 0
    for i in x:
        if int(i) > max:
            max = int(i)
    return max        

#####################
for line in lines[:]:
    answer = []
    pointer = -12
    #print("+++++++++++")
    temp = line[:pointer]
    max = next(temp)
    #print(max)
    answer.append(str(max))
    #print("-----------")
    for r in range(1,13):
        #print(f"=>{r}")
        temp = line[pointer:]
        #print(line)
        print(temp)
        max = next(temp)
        #print(max)
        answer.append(str(max))
        pointer += 1
    #print(f"+++>>>> {answer}")
    print("".join(answer))
    






#####################
print("----")
print()
