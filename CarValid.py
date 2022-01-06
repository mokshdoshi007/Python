import re 
s=input("Enter the Car Number: ")
m=re.fullmatch("GJ[0-3][0-9][A-Z]{2}[0-9]{4}",s)
if(m!=None): 
    print("Valid") 
else: 
    print("Invalid") 