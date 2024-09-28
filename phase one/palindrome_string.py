

# Function to check if the string is palindrome
def palindrome_str(str):

    start = 0
    end = len(str)-1
    while start <= end:
      if str[start] == str[end]:
        start += 1
        end -= 1
      else:
        print("String is not palindrome")
        return
    print("String is palindrome")
    

palindrome_str("radar")