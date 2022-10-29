# read() This prints out the entire file
with open('sample.txt', 'r') as file:
    print(file.read())

# read(n) This prints out n characters
with open('sample.txt', 'r') as file:
    print(file.read(10))

# readline() Prints out the first line
with open('sample.txt', 'r') as file:
    print(file.readline())

# readlines() Prints out multiple lines and able to iterate based on conditions
with open('sample.txt', 'r') as file:
    for x in file:
        print(x)