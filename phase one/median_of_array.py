def find_median(arr):
    arr.sort()  # Sort the array
    n = len(arr)

    # If the length is even, the median is the average of the middle two elements
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    # If the length is odd, the median is the middle element
    else:
        median = arr[n // 2]

    return median

# Example usage
array = [3, 1, 4, 1, 5, 9]
median_value = find_median(array)
print(f"The median is: {median_value}")
