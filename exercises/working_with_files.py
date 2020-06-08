import os

os.getcwd()
>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python33/README.txt")  # specifying full path

# either create a filen named a.txt beforehand so that we can read from it or provide an existing file name like Zen of python

f=open('a.txt')
for line in f:
    print(line)

# see the extra blank lines due to print command
# the print() has an "end parameter" to avoid two newlines when printing.

f.seek(0)   # go to the beginning of file before reading it again, see what happens if you omit this seek(0) command

for line in f:
    print(line, end='')

#Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
f = open("test.txt",mode = 'r',encoding = 'utf-8')

#read()		#return one big string
#readline	#return one line at a time
#readlines	#returns a list of lines

f.seek(0)
# check usage of seek() 

>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

>>> f.readline()
'This is the first line of the file.\n'

>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''


>>> for line in f:
       print(line, end='')

This is the first line of the file.
Second line of the file

#If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().


# write ()	#Used to write a fixed sequence of characters to a file
# writelines()	#writelines can write a list of strings.
# f.write(string) writes the contents of string to the file, returning the number of characters written.

>>>
>>> f.write('This is a test\n')
15

"""f.tell() returns an integer giving the file object’s current position
in the file represented as number of bytes from the beginning of the file
when in binary mode and an opaque number when in text mode.
"""

"""To change the file object’s position, use f.seek(offset, from_what).
The position is computed from adding offset to a reference point;
the reference point is selected by the from_what argument.
A from_what value of 0 measures from the beginning of the file,
1 uses the current file position, and
2 uses the end of the file as the reference point.
from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
"""

>>> # test.txt contents:
>>> # ABCDE
>>> f = open(r'C:\test.txt')
>>> f.seek(3)
>>> f.read()   # starts reading from the 3rd character
'DE'

>>> f = open(r'C:\test.txt')
>>> f.seek(2)    # move two characters ahead
>>> f.seek(2, 1) # move two characters ahead from the current position
>>> f.read()
'E'

>>> f = open(r'C:\test.txt')
>>> f.seek(-3, 2) # move to the 3rd character from the end of the file
>>> f.read()
'CDE'


>>> f = open('workfile', 'w') #opening mode:normal write
		    
>>> f.write('0123456789abcdef')
		    
16
>>> f.seek(5)
5

>>> f = open('workfile', 'wb+') #opening mode:binary write
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'

"""NOTE : In text files (those opened without a b in the mode string),
only seeks relative to the beginning of the file are allowed
(the exception being seeking to the very file end with seek(0, 2)) and
the only valid offset values are those returned from the f.tell(), or zero.
Any other offset value produces undefined behaviour.
"""

# CLOSING a FILE
# A safer way is to use a try...finally block.

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
"""
This way, we are guaranteed that the file is properly closed even if an exception is raised, causing program flow to stop.

The best way to do this is using the with statement. This ensures that the file is closed when the block inside with is exited.

We don't need to explicitly call the close() method. It is done internally.
"""
with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations
