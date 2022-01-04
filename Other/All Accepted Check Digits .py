ISBN = '10000'
test = 0

while int(ISBN) < 50000:
  num1 = int(ISBN[0])
  num2 = int(ISBN[1])
  num3 = int(ISBN[2])
  num4 = int(ISBN[3])
  multiplied1 = (num1*5)
  multiplied2 = (num2*4)
  multiplied3 = (num3*3)
  multiplied4 = (num4*2)
  allnum = (multiplied1+multiplied2+multiplied3+multiplied4)
  modulo = allnum%11
  finalnumber = 11-modulo
  number=int(ISBN[4])

  if finalnumber == number:
      print(ISBN)



  ISBN = int(ISBN) +1
  ISBN = str(ISBN)
