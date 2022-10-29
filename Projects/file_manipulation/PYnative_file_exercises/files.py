# # Creates a new empty text file named 'sales.txt 
# # x --> Open a file only for exclusive creation. If the file already exists, this operation fails.
f = open('sales.txt', 'x')
f.close()



# # Access mode w creates and writes content into a file
f = open('sales_2.txt', 'w')
f.write('first line')
f.close()


# # Verifying files
import os
# list files from a working directory
print(os.listdir())
# # Output: ['files.py', 'sales.txt', 'sales_2.txt']

# # verify file exists
print(os.path.isfile('sales.txt'))
# # Output: True


# # Creating a file in a specific directory
# # pass is used as a placeholder for future code
with open('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt', 'w') as f:
    f.write('This is the first line in the file')
    pass


# file paths
import os

# list files in directory
print(os.listdir('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises'))
# # Output: ['files.py', 'sales.txt', 'sales_2.txt', 'profot.txt']

# # verify file exists
print(os.path.isfile('/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt'))
# # Output: True



# # Joining a directory path and file name
import os 
path = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/account'
file_name = 'revenue.txt'

with open(os.path.join(path, file_name), 'w') as f:
    f.write('This is a new line')



# # Creating a file if it doesnt exist
import os

file_path = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/profot.txt'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as f:
        f.write('This is the first line')



# # Creating a file with a datetime
from datetime import datetime
# gets current date and time
x = datetime.now()

# # creates a file with date as a name day-month-year
file_name = x.strftime('%d-%m-%Y.txt')
with open(file_name, 'w') as file:
    print('created', file_name)
#     # output created 29-10-2022.txt

# # creates a file with day-month-year-hour-minute-second
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_2, 'w') as file:
    print('created', file_name_2)
#     # output created 29-10-2022-11-48-34.txt

# # creates a file at specific directory
file_name_3 = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/account//' + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as file:
    print('created', file_name_3)
#     # output: created /Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/account//29-10-2022-11-48-34.txt


# Creating a file with permission
"""Let’s see how to create a file with permissions other users can write.

To create a file with appropriate permissions, use os.open() to create the file descriptor and set the permission.
Next, open the descriptor using the built-in function open()"""

import os

file_path = '/Users/ev/learning-py/Projects/file_manipulation/PYnative_file_exercises/sample.txt'

# The default umask is 0o22 which turns off write permission of group and others
os.umask(0)
with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fh:
    fh.write('content')