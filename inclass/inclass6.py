

import os

dir()
dir(os)
a=3
dir()
dir(a)
import sys
dir(sys)


'''

os.chdir('C:')
os.chdir('/Users/metehangelgi/Destkop/summer19/engr350/inclass')
os.path.isfile('DNA_count.txt')

'''
print(os.getcwd()) # gets directory

try:
    with open("mete.txt","r+") as file:
        line=file.readline()
except(FileNotFoundError):
    print("I couldn't file at all")

mete=["1","2","3","4"]
print("*".join(mete))




'''
"*".join()
while line is not '':  ------> for file which you don't know length
file.seek(x)  ----> finds x and contiunes from here in next command  
r,w,a----
rb,wb,....for not txt files (cvs..)
'a aa bb d'.split()  -seperate with spaces
'absbdfgb'.split('b')- seperates from b 

'''

"""
------------------------------------------HW---------------------------------------------------
do file operation exercises...

------------------------------------------HW2---------------------------------------------------
dna_count.py olanı incele ...
------------------------------------------HW3---------------------------------------------------
decision tree kodlamasını öğren...
"""
print()


"""
Decision Tree:
Bool_Case.pdf
true data set 
derinlik everyone haricinde olanlardan aşağı inerek say 

80050 6404 320200
182600 8874 292842
236800 8300 149400
199100 5850 40950
698550 29428 803392
"""



"""
parametric and non parametric method

non-parametric:
classification
regression
CART- <<decision tree>> classs. and regres. tree


"""

