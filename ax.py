from typing import List

def missing_number(numbers: List[int]) -> int:
    n = len(numbers) + 1
    sum_expected = n * (n + 1) // 2

    sum_actual = sum(numbers)

    missing_number = sum_expected - sum_actual

    return missing_number

numbers = [1, 2, 3, 4, 6, 7, 8]
print(missing_number(numbers))