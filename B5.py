file=open("data.txt",mode='r')
f=file.readlines()
n=int(input("Enter value of n: "))
for i in range (n):
    print(f[len(f)-i-1])
file.close()