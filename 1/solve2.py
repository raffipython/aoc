import os
# 7299 is too high
# 6723 is too high
# 3797 is too low
# 6350 is bad
# 6219 is 
# 6490 is bad
# 6910 is bad
# 6701 is bad
# 6659 wrong
# 6671 right


DIAL_SIZE = 100
START = 50
FILENAME = "input3"   # change to "input" or "input2" as needed

def count_zero_hits(filename: str, start: int = START, dial_size: int = DIAL_SIZE) -> int:
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    current = start
    counter = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        step = -1 if direction == "L" else 1

        for _ in range(amount):
            current = (current + step) % dial_size
            if current == 0:
                counter += 1

        print(f"{line:>5} → dial at {current:3}, counter = {counter}")

    return counter


if __name__ == "__main__":
    total = count_zero_hits(FILENAME)
    print("\n--------")
    print(f"Final counter is: {total}")
