from typing import List
def rotated_sorted_array(numbers: List[int]) -> int:
    left, right = 0, len(numbers) - 1

    while left <= right:
        if numbers[left] <= numbers[right]:
            return left
        
        mid = (left + right) // 2
        next_mid = (mid + 1) % len(numbers)

        if numbers[mid] > numbers[next_mid]:
            return next_mid
        
        if numbers[mid] >= numbers[left]:
            left = mid + 1
        else:
            right = mid - 1

    return 0

numbers = [5, 6, 7, 8, 8, 9, 10, 1, 2, 3]
print(rotated_sorted_array(numbers))
