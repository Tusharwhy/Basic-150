def second_largest(arr):
    first = second = float('-inf')  # Initialize first and second to negative infinity
    
    for num in arr:
        if num > first:
            second = first  # Update second to be the previous largest
            first = num     # Update first to be the new largest
        elif first > num > second:
            second = num    # Update second if the current number is between first and second
    
    return second if second != float('-inf') else None  # Return second, or None if no second largest exists

# Example usage
numbers = [3, 5, 7, 2, 8, 10, 10, 10, 6]
result = second_largest(numbers)
print("The second largest number is:", result)
