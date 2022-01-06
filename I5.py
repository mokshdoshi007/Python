from collections import Counter
file=open("data.txt",mode='r')
print(Counter(file.read().split()))
file.close()