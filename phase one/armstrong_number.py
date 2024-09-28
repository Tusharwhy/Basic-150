# An Armstrong number is a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits in the number. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153

def armstrong_number(number):
  num_str = str(number)
  num_len = len(num_str)
  temp = 0
  
  for i in range(0,num_len):
    power = int(num_str[i]) ** num_len
    temp += power
  
  print(temp)
  if temp == number:
    print("Its an armstrong number")
  else:
    print("Not an armstrong number")
    
armstrong_number(154)