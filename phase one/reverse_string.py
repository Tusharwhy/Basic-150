def reverseString(name):
  start = ''
  for i in name:
    start = i + start
  print(start)


reverseString("name")