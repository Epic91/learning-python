# Creates a new empty text file named 'sales.txt 
# x --> Open a file only for exclusive creation. If the file already exists, this operation fails.
f = open('sales.txt', 'x')
f.close()



# Access mode w creates and writes content into a file
f = open('sales_2.txt', 'w')
f.write('first line')
f.close()


# Verifying files
import os
# list files from a working directory
print(os.listdir())
# Output:
# ['files.py', 'sales.txt', 'sales_2.txt']

# verify file exists
print(os.path.isfile('sales.txt'))
# Output
# True


# Creating a file in a specific directory
# pass is used as a placeholder for future code
with open('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt', 'w') as f:
    f.write('This is the first line in the file')
    pass


#import os

# list files in directory
print(os.listdir('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises'))
# Output: ['files.py', 'sales.txt', 'sales_2.txt', 'profot.txt']

# verify file exists
print(os.path.isfile('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt'))
# Output: True



# Joining a directory path and file name
import os 
path = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/account'
file_name = 'revenue.txt'

with open(os.path.join(path, file_name), 'w') as f:
    f.write('This is a new line')


# Creating a file if it doesnt exist
import os

file_path = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as f:
        f.write('This is the first line')