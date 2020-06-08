#import sys
import os

# get current working directory
# see the difference of the two commands' output
os.getcwd()
print(os.getcwd())
#'C:\\Users\\m\\AppData\\Local\\Programs\\Python\\Python36'
#'C:\Users\m\AppData\Local\Programs\Python\Python36'

# change directory
# in the following statements replace "c:\BANU" with the path according to your laptop directory structure
os.chdir(r'c:\ENGR350_codes')
os.getcwd()
#
print(os.getcwd())


#Creating New Folders with os.makedirs()
os.mkdir('c:\ENGR350_codes')
path='c:\ENGR350_codes'
os.chdir(path)
os.getcwd()

# run either of the following 2 mkdir statements
os.mkdir('c:\ENGR350_codes\DENEME') #absolute path
os.mkdir('DENEME')  #relative path

path='c:\ENGR350_codes\DENEME'
os.chdir('c:\ENGR350_codes\DENEME')
os.chdir(path)
print(os.getcwd())

os.getcwd()

#Check whether the directory has been created
os.path.abspath('.')

# seperators are OS dependent eg differs in Windows and unix
print(os.sep)
a,b = os.path.split(path)
a,b
os.path.join(a,b)

os.path.splitdrive(path)

path='c:\ENGR350_codes\DENEME'

os.path.basename(path)
os.path.dirname(path)
#

path='c:\ENGR350_codes\DENEME'
path

os.path.isfile(path)
os.path.isdir(path)

#
os.chdir("c:\ENGR350_codes\DENEME")
os.getcwd()

# to check if the file's path I want to create seems correct, 
# this file will be created in the local directory
os.getcwd()+"Deneme_metni.txt"

f=open(os.getcwd()+"\\Deneme_metni.txt")
for line in f:
	print(line.strip())
	

os.listdir('C:\\')
#how to print one directory at a line
print(os.listdir('C:\\'))
#does using a list print properly?
L1=os.listdir('C:\\')
print(L1)
#what about this?
for a in L1:
    print(a)

import os
import sys
#run a windows command from python
def os_system_sample():
    # Now system
    if sys.platform == 'win32':
        print("Running on a windows platform")
        command = "cmd.exe"

    if sys.platform == 'linux2':
        print("Running Linux")
        command = "uname -a"

    os.system(command)

# Prints subdirectory names of a given path
def subdirs(path):
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
	    print(entry.name)

# running shell commands from within python into a variable
a=os.popen('dir').read()

