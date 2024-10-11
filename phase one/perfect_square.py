import math

def is_perfect_square(number):
    if number < 0:
        return False
    
    # Calculate the square root of the number
    sqrt = int(math.sqrt(number))
    
    # Check if the square of the calculated square root equals the number
    return sqrt * sqrt == number

# Example usage
number = 16
print(f"Is {number} a perfect square? {is_perfect_square(number)}")
