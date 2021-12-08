from pathlib import Path
from itertools import combinations_with_replacement, product


def transpose_lists(all_list, index):
    return [x[index] for x in all_list]


def gamma_rate(values) -> str:
    gamma = []
    for x in values:
        res: dict
        res = {i: x.count(i) for i in set(x)}
        gamma.append("1" if res.get("1", 0) >= res.get("0", 0) else "0")
    return "".join(gamma)


def epsilon_rate(values):
    epsilon = []
    for x in values:
        res: dict
        res = {i: x.count(i) for i in set(x)}
        epsilon.append("0" if res.get("1", 0) >= res.get("0", 0) else "1")
    return "".join(epsilon)


def oxygen_rate(values: list, i: int = 0):
    remaining_val = values
    transposed_remaining_values = transpose_lists(remaining_val, i)
    count0 = transposed_remaining_values.count("0")
    count1 = transposed_remaining_values.count("1")
    if count1 >= count0:
        remaining_val = [x for x in remaining_val if x[i] == "1"]
    else:
        remaining_val = [x for x in remaining_val if x[i] == "0"]

    if len(remaining_val) > 1:
        return oxygen_rate(remaining_val, i + 1)
    else:
        return remaining_val


def dioxide_scrubber(values: list, i: int = 0):
    remaining_val = values
    transposed_remaining_values = transpose_lists(remaining_val, i)
    count0 = transposed_remaining_values.count("0")
    count1 = transposed_remaining_values.count("1")
    if count1 >= count0:
        remaining_val = [x for x in remaining_val if x[i] == "0"]
    else:
        remaining_val = [x for x in remaining_val if x[i] == "1"]
    if len(remaining_val) > 1:
        return dioxide_scrubber(remaining_val, i + 1)
    else:
        return remaining_val


values = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
values = (Path(__file__).parent / 'input.txt').read_text().splitlines()


bit_lengths = len(values[0])
values_as_tuples = [list(x) for x in values]

transposed = []

for idx in range(0, bit_lengths):
    transposed.append(transpose_lists(values_as_tuples, idx))

gamma_string = gamma_rate(transposed)
epsilon_string = epsilon_rate(transposed)

gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)
print(f"CONSUMPTION: {gamma*epsilon}")

oxygen_generator_rating = int(oxygen_rate(values).pop(), 2)

print(f"OXYGEN GENERATOR: {oxygen_generator_rating}")

oxygen_scrubber = int(dioxide_scrubber(values).pop(), 2)

print(f"CO2 Scrubber: {oxygen_scrubber}")

print(f"ANSWER: {oxygen_generator_rating*oxygen_scrubber}")