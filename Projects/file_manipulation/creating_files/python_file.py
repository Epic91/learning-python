# Writes a single line
with open('newfile.txt', 'w') as file:
    file.write('This is a new file I created!')

# Writes multiple lines
with open('newfile.txt', 'w') as file:
    file.writelines(['This is a new file I created!', '\nThis is another line to be added '])

# Adding to a file as opposed to replacing what was there.
with open('newfile.txt', 'a') as file:
    file.writelines(['\nThis is a new file I created!', '\nThis is another line to be added '])

# Using exceptions
try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(['\nThis is a new file I created!', '\nThis is another line to be added '])
except FileNotFoundError as e:
    print('ERROR', e)