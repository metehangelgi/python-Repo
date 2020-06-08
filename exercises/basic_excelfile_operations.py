""" see read_excel() similar to read_csv() check documentation at
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html In order to be able to use it
YOU WILL NEED to install xlrd module via pip or similar for read_excel() 
"""
import xlrd
df1=pd.read_excel('uk-500.xlsx')
df1.head()

# see you don't need to open the file beforehand,
# you can directly read into the dataframe using this method of pandas

# reading from a particular sheet of the excel file
df2=pd.read_excel('uk-500.xlsx',sheet_name='uk-500')
df2.head()
