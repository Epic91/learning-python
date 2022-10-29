# read()
with open('samplefile,txt' 'r') as file:
    print(file.read())

# read(n) with an integer as an argument
with open('samplefile,txt' 'r') as file:
    print(file.read(40))

# readline()
with open('samplefile,txt' 'r') as file:
    print(file.readline())

# readline(n)
with open('samplefile,txt' 'r') as file:
    print(file.readline(10))

# readlines()
with open('samplefile,txt' 'r') as file:
    lines = file.readlines()
    print(len(lines))
