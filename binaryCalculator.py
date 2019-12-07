def getQR(num):
  Q=num//2
  R=num%2
  return Q,R

def getBinary(num):
  Q=1
  converted=""

  while (Q>0):
    Q,R=getQR(num)
    num=Q
    converted=str(R)+converted
    
  converted=int(converted)
  return converted

def onesComplement(num):
  num=str(num)
  newnum=""
  for bit in num:
    if bit=='1':
      bit='0'
    elif bit=='0':
      bit='1'
    newnum+=bit
  return newnum

def twosComplement(num):
  num=str(num)
  newnum=""
  if num[-1]=='1':
    revNum=""
    newnum=""
    for bit in num:
      revNum=bit+revNum
    carry='1'
    for bit in revNum:
      if carry=='1':
        if bit=='1':
          newnum='0'+newnum
          carry='1'
        else:
          newnum='1'+newnum
          carry='0'
      else:
        if bit=='1':
          newnum='1'+newnum
        else:
          newnum='0'+newnum
  else:
    newnum=num[:-1]+'1'
    
  return newnum

def bitSize(num,size):
  num=str(num)
  toAdd=size-len(num)
  
  bitNum='0'
  
  newnum=""
  newnum=bitNum*toAdd
  newnum=newnum+num
  return newnum

def bitSize(num,size):
  num=str(num)
  toAdd=size-len(num)
  
  bitNum='0'
  #1 for neg
  #0 for pos 

  newnum=""
  newnum=bitNum*toAdd
  newnum=newnum+num
  return newnum

def checkOverflow(num,size):
  num=str(num)
  if len(num)>size:
    sizeCut=(len(num))-size
    newnum=num[sizeCut:]
  else:
    newnum=num

  return newnum

def reverse(s):
  revS=""
  for l in s:
    revS=l+revS
  return revS
def binAdd(num1,num2):
  num1=str(num1)
  num2=str(num2)

  if len(num1)!=len(num2):
    if len(num1)>len(num2):
      diff=len(num1)-len(num2)
      num2=('0'*diff)+num2
    if len(num2)>len(num1):
      diff=len(num2)-len(num1)
      num1=('0'*diff)+num1

  revNum1=reverse(num1)
  revNum2=reverse(num2)

  newnum=""
  carry='0'
  position=0

  for bit in revNum1:

    if bit=='1':
      if revNum2[position]=='1':
          if carry=='1':
            carry='1'
            newnum='1'+newnum
          elif carry=='0':
            carry='1'
            newnum='0'+newnum

      elif revNum2[position]=='0':
          if carry=='1':
            newnum='0'+newnum
            carry='1'
          elif carry=='0':
            newnum='1'+newnum
            carry='0'

    elif bit=='0':  
      if revNum2[position]=='1':
        if carry=='1':
          newnum='0'+newnum
          carry='1'
        elif carry=='0':
          newnum='1'+newnum
          carry='0'

      elif revNum2[position]=='0':
        if carry=='1':
          newnum='1'+newnum
          carry='0'
        elif carry=='0':
          newnum='0'+newnum
          carry='0'

    position+=1

  if carry=='1':
    newnum='1'+ newnum

  return newnum

def sameLen(num1,num2):
  num1=str(num1)
  num2=str(num2)

  if len(num1)!=len(num2):
    if len(num1)>len(num2):
      diff=len(num1)-len(num2)
      num2=('0'*diff)+num2
    if len(num2)>len(num1):
      diff=len(num2)-len(num1)
      num1=('0'*diff)+num1
  
  return num1,num2
      

        


