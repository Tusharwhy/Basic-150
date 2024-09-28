
# we know its a leap year if it follows these conditions
# Divisible by 4: Leap year if it is not divisible by 100.
# Divisible by 100: Not a leap year unless it is also divisible by 400.
# Divisible by 400: Always a leap year.

def leap_year(year):
  if year % 400 == 0:
    print("Its a leap year")
  elif year % 4 == 0 and year % 100 != 0:
    print("Its a leap year")
  else:
    print("Its not a leap year")
    
    
leap_year(1900)