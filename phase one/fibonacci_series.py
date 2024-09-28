




#inital approach
def fibonacci_one(limit):
  arr = [0,1]
  a = arr[0]
  b = arr[1]
  c = a + b
  
  for i in range(2,limit):
    arr.append(c)
    a = b
    b = c
  print(arr)
  

#Improved approach
def fibonacci_two(limit):
  if limit <= 0:
     print([])
     return
  elif limit == 1:
    print([0])
    return
    
  arr = [0,1]
  for i in range(2,limit):
    arr.append(arr[-1] + arr[-2])
 
  print(arr)
  
  
