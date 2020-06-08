import os

print("Example_str_join.txt")
print("the_Zen_Of_Phyton.txt")
print("words.txt")
print("top_selling_albums.csv")
print("UK-500.csv")
print("UK-500.xlsx")
print("iris.csv")
print("tips.csv")

print("our path is >>>> /Users/metehangelgi/Desktop/summer19/engr350/exercises")
#1


pathName=''
while os.path.isdir(pathName) is not True:
    pathName=input("please enter your path: ")


line=" "
paragraphList=list()
try:
    fileName=input("please enter your file name: ")
    with open(pathName+"/"+fileName,"r") as file:
        while line is not '':
            line=file.readline()
            paragraphList.append(line)

except(FileNotFoundError):
    print("not file found")
paragraph=""
for i in paragraphList:
    paragraph=paragraph+i


paragraph=paragraph.replace("\n"," ")
paragraph=paragraph.replace(". ",".\n")


try:
    fileName2=input("please enter location of file and file name (File name should be: Example_joined_paragraph.txt")
    with open(fileName2,"w") as file2:
        file2.write(paragraph)

except(FileNotFoundError):
    print("not found such file")



#2
line=" "
paragraph2=""
try:
    with open("the_Zen_Of_Phyton.txt",encoding = 'utf-8') as file3:
        while line is not '':
            line=file3.readline()
            paragraph2=paragraph2+line
except(FileNotFoundError):
    print("not found that file")

print(paragraph2)

#3

import string


paragraph2=paragraph2.lower()
letters= list(string.ascii_lowercase)


all(c in paragraph2 for c in letters)  # if asks are they have letters but to find letter I couldn't use it
unfoundLetters=list()
try:

    for letter in letters:
        index=paragraph2.find(letter)
        if index < 0:
            unfoundLetters.append(letter)
except(ValueError):
    print(letter, "is not in the paragraph")

print(unfoundLetters)

#4


try:
    words=list()
    words2=""
    words2List=list()
    line=" "
    with open("words.txt","r+") as file4:
        while line is not '':
            line=file4.readline()
            words.append(line)
        file4.seek(0)
        line = " "
        while line is not '':
            line=file4.readline()
            words2=words2+line
        words2List=words2
except(FileNotFoundError,KeyError):
    print("error")


#5

import csv
import sys
import pandas as pd

'''
with open("LifeExp.csv", "rb") as file5: # rb is reader --- wb is writer
    reader = csv.reader(file5)
    for row in reader:
        print (row)
'''
"""

with open("LifeExp.csv", "rb") as file5: # rb is reader --- wb is writer
    readerMe=csv.reader(file5,delimiter=',')
    line_count = 0
    for row in readerMe:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""

data = pd.read_csv("LifeExp.csv")
print(data.head())

print(data)
line=" "
LineList=list()
lineCounter=0
try:
    with open("LifeExp.txt") as file5:
        while  line is not '':
            line=file5.readline()
            LineList.append(line)
            lineCounter+=1
except(FileNotFoundError):
    print("no found file")

WordsInList=list()
for lines in LineList:
    WordsInList.append(lines)

print(lineCounter)
print(WordsInList.__sizeof__())
letterCounter=0

for i in WordsInList:
    letterCounter+=i.__sizeof__()

print(letterCounter)
print(data.head(10))

#6

import xlrd

listOfDataFiles=["LifeExp.csv","uk-500.csv","tips.csv","mobile_services_ranking.csv"]

for CurrentFile in listOfDataFiles:
    data2 = pd.read_csv(CurrentFile)
    print(data2) #1
    for i in data2:
        print(i) #2
    number=int(input("please enter how many lines you want: "))
    print(data2.head(number)) #3
    print()
    print(data2.cov(10))
data3= pd.read_excel("uk-500.xlsx")
print(data3)



