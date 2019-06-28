def nexPolindrom(number):
    flag = polindrom(number)
    if type(number)=='str':
        return flag, number
    if type(number)=='int':
        if flag==True:
            return flag, number
        else:
            number = number + 1
            nexPolindrom(number)
            
    

def polindrom(number):
    temp = str(number)
    if temp == temp[::-1]:
        return True
    else:
        return False

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


