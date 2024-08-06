

def second_largest(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return None 
    
    first_max = second_max = float('-inf')
    
    for num in numbers:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max

numbers = [1, 2, 3, 4, 5]
print(second_largest(numbers))
