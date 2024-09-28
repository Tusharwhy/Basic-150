num = [8,5,6,5,8]


def check_numbers(num):
  start = 0
  end = len(num)-1
  mid = len(num)//2

  while(start <= end):
    if(num[start] == num[end]):
      start += 1
      end -=  1
    else:
      print("Numbers are not palindrome")
      return 
    
  print("Numbers are palindrome")
    
    
check_numbers(num)
      