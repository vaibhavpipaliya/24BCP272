def count_alphabets():
  string= input("string : ")
  b=0
  c=0
  for ch in string:
      if ch.isalpha():
        c=c+1
      elif ch.isdigit():
        b=b+1      
  print ("alphabets",c)
  print ("digits",b)
count_alphabets()
