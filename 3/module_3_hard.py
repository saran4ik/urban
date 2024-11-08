def calculate_structure_sum(data):
    sum_d = 0
    if isinstance(data, dict):
        data = list(data.items())
    for d in data:
        if isinstance(d, (int, float)):
            sum_d += d
        elif isinstance(d, str):
            sum_d += len(d)
        else:
            sum_d += calculate_structure_sum(d)
    return sum_d


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)
