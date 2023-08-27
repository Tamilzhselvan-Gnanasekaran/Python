def primeproduct(m):
    x=[]
    for i in range(2,m+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            x.append(i)
    for i in range(0,len(x)):
        for j in range(0,len(x)):  
            if(x[i]*x[j]==m):
                return True 
    else:
        return False
      
      

      
def delchar(s,c):
    if len(c)==1:
        s=s.replace(c,'')  
        return (s)
    else:
        return (s)
      
      
      
def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])      
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])      
    return (c)      
      
      

      
###

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primeproduct":
   arg = parse(farg)
   print(primeproduct(arg))
elif fname == "delchar":
   (s1,s2) = parse(farg)
   print(delchar(s1,s2))
elif fname == "shuffle":
   (l1,l2) = parse(farg)
   print(shuffle(l1,l2))
else:
   print("Function", fname, "unknown")
