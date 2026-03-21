import os
'''
file_path = "example"
file = open(file_path, "r")

content = file.read()
print(content)
file.close()

file_path = "example"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
'''
with open('example', "r") as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()


#Writing to Files
with open('example', 'w') as file:
    file.write("hello, world")


lines =["Hello world\n", "welcome to Python ADV\n"]

with open('example', 'r') as file:
    file.seek(0)
    data = file.read()
    print(data)

if os.path.exists('example'):
    print("file exists")


with open('example', 'a') as file:
    file.write("new data appended")

data = b'this is some binary data'
with open('example', 'wb') as file:
    file.write(data)

with open('binary_fille.bin', 'rb') as binary_file:
    data = binary_file.read()