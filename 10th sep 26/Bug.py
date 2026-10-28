def group_numbers(numbers):
    result = {
        "even": [],
        "odd": []
    }


test_cases = [
    [1, 2, 3, 4, 5, 6],
    [0, -1, -2, 7],
    [],
]

for case in test_cases:
    print(f"Input:  {case}")
    print(f"Output: {group_numbers(case)}")