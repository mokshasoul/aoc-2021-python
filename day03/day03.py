
def transpose_lists(all_list, index):
    return [x[index] for x in all_list ]

def gamma_rate(values):
    gamma = []
    for x in values:
        res: dict
        res = {i: x.count(i) for i in set(x)}
        gamma.append('1' if res.get('1',0) > res.get('0',0) else '0')
    return gamma

def epsilon_rate(values):
    epsilon = []
    return epsilon

values = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010', ]


values_as_tuples = [list(x) for x in values]

transposed = []
for idx in range(0,5):
    transposed.append(transpose_lists(values_as_tuples, idx))

print(gamma_rate(transposed))