# I used uk-500.csv as the csv file for this code, you can use any csv type file
import sys
import os

# READING FROM csv FILE
# use one of the following approaches
# create a variable holding the path and the name of the csv file

#csvfilename=
csvfilename=input('File name:')
#csvf1=open(<csvfilename>,"r")
#OR provide the fullpath and filename as a string parameter
csvf1=open(csvfilename,"r")

#csvf1 is our file handle within the code whenever we need to refer the file we will use it

# what do you expect to see when you print the file handle
print(csvf1)

input('press a key...')

print(csvf1.readline())
#first_name,last_name,company_name,address,city,county,postal,phone1,phone2,email,web

input('press a key...')

csvf1.tell()
input('press a key...')

line1=csvf1.readline()
print(line1)
#Aleshia,Tomkiewicz,Alan D Rosenburg Cpa Pc,14 Taylor St,St. Stephens Ward,Kent,CT2 7PP,01835-703597,01944-369967,atomkiewicz@hotmail.com,http://www.alandrosenburgcpapc.co.uk

line_contents=line1.split(',')
print(line_contents)
#['Aleshia', 'Tomkiewicz', 'Alan D Rosenburg Cpa Pc', '14 Taylor St', 'St. Stephens Ward', 'Kent', 'CT2 7PP', '01835-703597', '01944-369967', 'atomkiewicz@hotmail.com', 'http://www.alandrosenburgcpapc.co.uk\n']

input('press a key...')

csvf1.seek(0,0)
print(csvf1.readline())

input('press a key... before file hndle copy')

f=csvf1

for i in range(10):
	print(f.readline())

f.tell()
f.seek(0)
f.tell()
print(f.readline())


# READING using pandas module 
import pandas as pd
pd.read_csv(csvf1)
