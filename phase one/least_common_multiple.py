# LCM is just multiplication of (a * b)/(gcd(a,b))


def lcm(a,b):
  c = a * b
  my_gcd = gcd(a,b)
  result = c//my_gcd
  return my_gcd
  
  
# we use euclidean algorithm
def gcd(a,b):
  
  # we find GCD
    while b != 0:
      temp = a % b
      a = b
      b = temp 
    return a
  
your_lcm = lcm(4,6)

print(your_lcm)