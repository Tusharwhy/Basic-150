

def sum_digit(digits):
  # we assign the digits to num variable
  num = digits
  # temporary variable for storing sum
  temp = 0
  
  # loop should run untill our num becomes 0
  while num != 0:
    # we get last digit by modulo operator eg => 1234 % 10 = 4
    last_digit = num % 10
    # we add this last digit to temp variable
    temp += last_digit
    # and finally we remove the last digit eg 1234 // 10 => 123
    num= num // 10
  
    
  print(temp)
  
  
sum_digit(12345)