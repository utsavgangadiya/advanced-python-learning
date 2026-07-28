# read file data

f = open("file handling/hello.txt","r")

# data = f.read()
# print(data)

# readline


line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

f.close()