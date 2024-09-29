


def prime_number(num):
  is_prime = True
  
  for i in range(2,int(num**0.5)+1):
  
    if num % i == 0:
      is_prime = False
      break
  return is_prime
 
 
def in_range(arr):
  prime_numbers = []
  start = arr[0]
  end = arr[1] + 1
  for i in range(start, end):  
    is_prime = prime_number(i) 
    
    if is_prime:
      prime_numbers.append(i)
    
  return prime_numbers

 
print(in_range([10,20]))