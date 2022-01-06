import re 
s=input("Enter the Mail id --")
m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if(m!=None): 
    print("Email id is valid") 
else: 
    print("Email id is in valid") 