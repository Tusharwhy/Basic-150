
def start_pattern(height):
  for i in range(height):
    for j in range(height - i -1):
     print("*",end=" ")
     
        # Print stars, which increase in count each row
    for k in range(2 * i + 1):
        print("*", end="")
  
start_pattern(5)