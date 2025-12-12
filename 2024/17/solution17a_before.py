data = """Register A: 35200350
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0"""

data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

reg_a = 729
reg_b = 0
reg_c = 0
program = [0,1,5,4,3,0]

def helper(a, b, c, p):
    global reg_a
    global reg_b
    global reg_c
    global program
    reg_a = a
    reg_b = b
    reg_c = c
    program = p



# instructions
# opcode 0
def adv(x):
    combo = combo_return(x)
    global reg_a
    reg_a = int(reg_a / (2**combo))

# opcode 1
def bxl(x):
    literal = x
    global reg_b
    reg_b =  reg_b ^ literal

# opcode 2
def bst(x):
    global reg_b
    reg_b = x % 8

# opcode 3
def jnz(eip, x):
    global reg_a
    global reg_b
    global reg_c
    
    
    if reg_a == 0:
        return eip
    else:
        return eip + x

# opcode 4
def bxc(x):
    # x ignored
    global reg_b
    reg_b = reg_b ^ reg_c

# opcode 5
def out(x):
    combo = combo_return(x)
    global reg_b
    print(f"OUT: {combo % 8}")


# opcode 6
def bdv(x):
    global reg_b
    combo = combo_return(x)
    reg_b = int(reg_a / (2**combo))

# opcode 7
def cdv(x):
    combo = combo_return(x)
    global reg_c
    reg_c = int(reg_a / (2**combo))

def combo_return(x):
    if x == 0 or x == 1 or x == 2 or x == 3:
        return x
    elif x == 4:
        return reg_a
    elif x == 5:
        return reg_b
    elif x == 6:
        return reg_c
    elif x == 7:
        pass
    else:
        pass

def print_reg(eip):
    print("--------------")
    print(f"A:    {reg_a}")
    print(f"B:    {reg_b}")
    print(f"C:    {reg_c}")
    print(f"EIP:  {eip}")
    print(f"Prog: {program}")    
    print(">>>>>>>>>>>>>>")




helper(2024, 0, 0, [0,1,5,4,3,0])

eip = 0
print_reg(eip)
print("\n\n")
while eip < len(program):
    print(f"LENGTH: {len(program)}")
    p = program[eip]
    if p == 0:
        adv(p)
    elif p == 1:
        bxl(p)        
    elif p == 2:
        bst(p)        
    elif p == 3:
        eip = jnz(eip, p)        
    elif p == 4:
        bxc(p)       
    elif p == 5:
        out(p)        
    elif p == 6:
        bdv(p)        
    elif p == 7:
        cdv(p)    

    eip = eip + 1
    

    print_reg(eip)
    input()


