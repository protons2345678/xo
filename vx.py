from typing import List
def number_of_occurences(numbers: List[int], target: int) -> None:
    count = 0
    first_index = None
    last_index = None

    for i in range(len(numbers)):
        if numbers[i] == target:
            if first_index is None:
                first_index = i
                last_index = i
                count += 1

    if count > 0:
        print(f"First index: {first_index}, Last index: {last_index}, Occurences: {count}")
    else:
        print(f"The target number {target} is not found in the list.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(number_of_occurences(numbers, 10))    
