def sum_digit(digits):
  num = digits
  temp = 0
  while num != 0:
    last_digit = num % 10

    temp += last_digit
 
    num= num // 10
  
    
  print(temp)
  
  
sum_digit(12345)