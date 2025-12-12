filename = 'test'
filename = 'input'
with open(filename, 'r') as fd:
    f = fd.read().split("\n")[:-1]

data = {}
for line in f:
    parts = line.split(":")
    numbers = parts[1].split(" ")
    numbers = numbers[1:]
    numbers = [int(x) for x in numbers]
    data.update({int(parts[0]):numbers})



from itertools import product


def evaluate_expressions(nums, k):
    operators = ['+', '*']
    n = len(nums)
    results = []

    # Generate all possible combinations of operators
    for ops in product(operators, repeat=n-1):
        # Manually evaluate the expression from left to right
        result = nums[0]
        expression = str(nums[0])
        
        for i in range(1, n):
            if ops[i-1] == '+':
                result += nums[i]
            elif ops[i-1] == '*':
                result *= nums[i]
            expression += f" {ops[i-1]} {nums[i]}"
       
        results.append((expression, result))
        if result == k:
            #print(k, result)
            return result
    return False




total = 0
#print(data)
for k in data.keys():
    #print(k)
    v = data.get(k)
    #print(v)
    #print(len(v))
    # Example usage:
    nums = v
    result = evaluate_expressions(nums, k)
    print(result)
    if result:
        total += result
    #for expr, value in results:
    #    print(f"{expr} = {value}")

print(total)



