# open function handling

file = open('test.txt', mode = 'r')

data = file.readline()

print(data)

file.close()
# readline will return the first line in the file
# readlines will output an array with multiple lines



# with open function handling
with open('test.txt', mode = 'r') as file:
    data = file.readline()
    print(data)