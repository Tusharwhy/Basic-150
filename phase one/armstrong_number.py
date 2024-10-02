
# An Armstrong number is a positive integer that is equal to the sum of its digits, each raised to the power of the number of digits in the number. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153

def armstrong_number(number):
  if number == 1:
    return True
  elif number < 10:
    return False

  num_str = str(number)
  num_len = len(num_str)
  temp = 0
  
  for i in range(0,num_len):
    power = int(num_str[i]) ** num_len
    temp += power
  
  if temp == number:
    return True
  
  return False
    
#GETTING  ARMSTRONG NUMBER IN RANGE
def armstrong_number_in_range(arr):
  start = arr[0]
  end = arr[1]
  temp = []
  for i in range(start, end+1):
    asNumber = armstrong_number(i)
    if asNumber:
      temp.append(i)
  return temp

numbers = armstrong_number_in_range([1,500])

print(numbers)