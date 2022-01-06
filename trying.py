file=open("data.txt",mode='r')
f=file.readlines()
try:
    for i in range (10):
        print(f[i],end="")
except IndexError:
    print("\nNo More Data to Show")
finally:
    file.close()