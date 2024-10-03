
# code for finding perfect number
def perfect_number(number):
  sum = 0
  for i in range(1,number):
    if number % i == 0:
      sum += i
      
  if sum == number:
    print("Its a perfect number")
    
perfect_number(28)