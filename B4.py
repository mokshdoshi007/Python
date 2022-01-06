file=open("data.txt",mode='r')
f=file.readlines()
n=int(input("Enter value of n: "))
for i in range (n):
    print(f[i])
file.close()