file=open("data.txt",'r')
l=file.readlines()
l=[x.rstrip('\n') for x in l]
print(l)