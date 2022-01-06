file=open("data2.txt",mode='w')
l=["Moksh","Age",19]
file.writelines("%s\n" % x for x in l)