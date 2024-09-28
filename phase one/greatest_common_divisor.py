# we use euclidean algorithm
def gcd(a,b):
    while b != 0:
      temp = a % b
      a = b
      b = temp 
    return a
  
your_gcd = gcd(4,6)

print(your_gcd)