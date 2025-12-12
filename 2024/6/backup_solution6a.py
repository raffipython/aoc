filename = 'input'
filename = 'test'
#filename = 'dontuse'

with open(filename, 'r') as fd:
    f = fd.read()

lines = f.split("\n")[:-1]
global array
array = []
for line in lines:
    array.append([i for i in line])

for line in array:
	print(line)
print("\n\n")

def up(array):
	print("\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	counter = 0
	for i in range(len(array)):
		try:
			y = array[i].index("^")
			x = i
		except:
			pass
	print(f"RIGHT: {y+1}	DOWN: {x+1}")
	
	array[x][y] = "x" # replace current guard
	path = []
	obs = False
	go_up = x - 1
	while not obs:
		try:
			if array[go_up][y] == "#":
				obs = True
			else:
				array[go_up][y] = "x"
			go_up -= 1
		except:
			print("END")
			obs = True
			return True
	
	#print(y)
	#print(x)
	#print(go_up+1)
	#print(array[go_up+1][y])	
	array[go_up+2][y+1] = ">"
	for line in array:
		print(line)
	#print(f"COUNTER: {counter}")
	return False

def right(array):
	print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	counter = 0
	for i in range(len(array)):
		try:
			y = array[i].index(">")
			x = i
		except:
			pass
	print(f"RIGHT: {y+1}	DOWN: {x+1}")
	
	array[x][y] = "x" # replace current guard
	path = []
	obs = False
	go_right = y + 1
	while not obs:
		try:
			if array[x][go_right] == "#":
				obs = True
			else:
				array[x][go_right] = "x"
			go_right += 1
		except:
			print("END")
			obs = True
			return True
	
	array[x+1][go_right-2] = "v"
	for line in array:
		print(line)

	#print(f"COUNTER: {counter}")
	return False

def down(array):
	print("\n\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
	counter = 0
	for i in range(len(array)):
		try:
			y = array[i].index("v")
			x = i
		except:
			pass
	print(f"RIGHT: {y+1}	DOWN: {x+1}")
	
	array[x][y] = "x" # replace current guard
	path = []
	obs = False
	go_down = x + 1
	while not obs:
		try:
			if array[go_down][y] == "#":
				obs = True
			else:
				array[go_down][y] = "x"
			go_down += 1
		except:
			print("END")
			obs = True
			return True
	
	print(y)
	print(x)
	print(go_down+1)
	print(array[go_down+1][y])	
	array[go_down-2][y-1] = "<"
	for line in array:
		print(line)

	#print(f"COUNTER: {counter}")
	return False

def left(array):
	print("\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
	counter = 0
	for i in range(len(array)):
		try:
			y = array[i].index("<")
			x = i
		except:
			pass
	print(f"RIGHT: {y+1}	DOWN: {x+1}")
	
	array[x][y] = "x" # replace current guard
	path = []
	obs = False
	go_left = y - 1
	while not obs:
		try:
			if array[x][go_left] == "#":
				obs = True
			else:
				array[x][go_left] = "x"
			go_left -= 1
		except:
			print("END")
			obs = True
			return True
	

	print(y)
	print(x)
	print(go_left+1)
	print(array[go_left+1][y])	
	array[x-1][go_left+2] = "^"
	for line in array:
		print(line)

	#print(f"COUNTER: {counter}")
	return False


end = False 

# 16900
#while not end:
for i in range(10):
	end = up(array)
	end = right(array)
	end = down(array)
	end = left(array)
	
	#end = True


print("\n###########################")
for line in array:
	print(line)

