


def prime_number(num):
  is_prime = True
  
  for i in range(2,int(num**0.5)+1):
    print(int(num**0.5))
    print( num % i)
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print("The Number is Prime")
  else:
    print("The Number is not Prime")
      
      
prime_number(10)