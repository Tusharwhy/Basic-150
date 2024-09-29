# in this code we find largest number and
# smallest number in array

def large_small(arr):
  smallest = arr[0]
  largest = arr[0]
  
  for i in range(len(arr)):
    #for smallest number
    if(arr[i] < smallest):
      smallest = arr[i]
    #for largest number
    if (arr[i] > largest):
      largest = arr[i]
      
  print("smallest number: ",smallest)
  print("largest number: ",largest)
  
  
large_small([4,5,1,2,3,0,8,99])