# code for finding out the even numbers

def even_numbers(arr):
  end = arr[1]
  sum = 0
  for i in range(1, end+1):
    if i % 2 == 0:
      sum += i
      
  print(sum)
    
    
even_numbers([1,10])