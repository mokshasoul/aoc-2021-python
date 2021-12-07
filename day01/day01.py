from pathlib import Path


input_file = Path(__file__).parent / "input.txt"

inputs = input_file.read_text().splitlines()
count_increase = 0
prev = 0
"""
inputs = [
199,
200,
208,
210,
200,
207,
240,
269,
260,
263
]
"""
for idx, number in enumerate(inputs):
    if idx == 0:
        prev = int(number)
        continue
    if int(number) > prev:
        count_increase += 1
    prev = int(number)

print(count_increase)
