#Following function is to sort array in asc to descc
#Input: array = [3, 1, 4, 1, 5, 9]
#Output: [1, 1, 3, 4, 5, 9]

def sort_arr(arr):
  temp = 0
  for i in range(len(arr)):
    for j in range (i+1, len(arr)):
     if (arr[i] > arr[j]):
       
      #  temp = arr[j]
      #  arr[j] = arr[i]
      #  arr[i] = temp
      # We can aslo swap like this:
       arr[i],arr[j] = arr[j],arr[i]
       
       
  print(arr)
  
  
sort_arr([3, 1, 4, 1, 5, 9])