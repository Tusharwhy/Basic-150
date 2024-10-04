def find_missing_numbers(sequence):
    n = max(sequence)  # Get the highest number in the given sequence
    complete_sequence = set(range(1, n + 1))  # Create a set with numbers from 1 to n
    given_sequence = set(sequence)  # Convert the given sequence into a set

    missing_numbers = list(complete_sequence - given_sequence)  # Find the difference
    return missing_numbers

sequence = [1, 2, 4, 5]
missing_numbers = find_missing_numbers(sequence)
print(missing_numbers)  # Output: [3]
