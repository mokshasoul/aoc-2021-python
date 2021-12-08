from pathlib import Path
import numpy as np

def part_one(inputs):
    count_increase = 0
    prev = 0
    for idx, number in enumerate(inputs):
        if idx == 0:
            prev = int(number)
            continue
        if int(number) > prev:
            count_increase += 1
        prev = int(number)
    return count_increase

def part_two(inputs):
    math_tuples = []
    for idx in range(0,len(inputs)-2):
        math_tuples.append((inputs[idx],inputs[idx+1], inputs[idx+2]))

    print(math_tuples)
    sums_window = list(map(sum,math_tuples))
    return sums_window 

input_file = Path(__file__).parent / "input.txt"


inputs = np.array([
    int(x) for x in input_file.read_text().splitlines()
    ]
)
# inputs = [
# 199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263,
# ]
print(part_one(inputs))
print(part_one(part_two(inputs)))