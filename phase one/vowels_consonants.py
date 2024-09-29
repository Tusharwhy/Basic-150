
#inital approach
def is_vowels(str):
  lwr_str = str.casefold()
  myset = {"a","e","i","o","u"}
  vowel_count = 0
  consonant_count =0 
  for i in lwr_str:
    if (i in myset):
      vowel_count += 1
    else:
      consonant_count +=1
      
  print("number of vowels: ",vowel_count)
  print("number of consonants: ",consonant_count)

#improved approach => here we also check if the letter is aplhabet or not? 
#else it will count spaces and character as consonants
def is_vowels(str):
  lwr_str = str.casefold()
  myset = {"a","e","i","o","u"}
  vowel_count = 0
  consonant_count =0 
  for i in lwr_str:
    if (i in myset):
      vowel_count += 1
    elif i.isalpha():
      consonant_count += 1

      
  print("number of vowels: ",vowel_count)
  print("number of consonants: ",consonant_count)
  
is_vowels("hello world")