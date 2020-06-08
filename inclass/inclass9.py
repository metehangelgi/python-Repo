import pandas as pd
import numpy as np






with open("LifeExp.csv") as file:
    dataFrame = pd.read_csv(file)
    print(type(dataFrame))
    print(dataFrame)
    print(dataFrame.describe())

    print(dataFrame.head(15),"\n")

    print(dataFrame.tail(5))
    print(dataFrame.cummin,"\n")

    print(dataFrame['country'])
    print(dataFrame['continent'].unique())

    print(len(dataFrame['continent']))
    print(dataFrame.country=='Turkey')
    print(dataFrame[dataFrame.country=="Turkey"]) #filtering
    print(dataFrame[dataFrame.country == "Albania"]) #filtering

    print(dataFrame[dataFrame.country.isin(['Turkey','Albania'])])


    dataFrame_TR=dataFrame[dataFrame.country.isin(['Turkey'])]
    print(dataFrame_TR.describe())

    print(dataFrame[dataFrame.lifeExp>=80])
    dataFrame_80=dataFrame[dataFrame.lifeExp>=80]
    print(len(dataFrame_80))

    dataFrame_80Continent = dataFrame_80[dataFrame_80.continent=='Oceania']
    print(dataFrame_80Continent)


    dataFrame_80Continent2=dataFrame_80[dataFrame_80.continent.isin(['Europe','Asia']) & dataFrame_80.year.isin([2007])]
    print(dataFrame_80Continent2)


    print(dataFrame[dataFrame.continent.isin(['Asia']) & (dataFrame.year.isin([2002])) & (dataFrame.lifeExp>=70)].sort_values(by='lifeExp'))



    dataFrame_1=dataFrame[(dataFrame.gdpPercap>=20000) & (dataFrame.year >=2002)].sort_values(by='lifeExp', ascending=False)

    print(dataFrame_1.drop_duplicates(subset='country'))


    """
    numpy Array vs pd.Series differences:(check on internet)
    
    
    https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
    
    excel içinde transpose yapmak için veriyi kopyala sonra özel yapıştırma seçenekleri içinde transpose var onu seç 
    
    """



s1=pd.Series([1,2,3,"mete",5])
print(s1)
s2=pd.date_range('20190805',periods=6)
print(s2)
s3=pd.date_range('20190805',periods=6,freq='W')
print(s3)
s4=pd.date_range('20190805',periods=6,freq='M')
print(s4)

df = pd.DataFrame(np.random.randn(6, 4), index=s4, columns=list('ABCD'))
print(df)

s5=pd.date_range('20190905',periods=14,freq='D')

df2=pd.DataFrame(np.random.randn(14,3),index=s5,columns=['A1','B2','C3'])

print(df2)



"""
numpy exercises



"""

kod=np.zeros((3,4)) # row,column

print(kod)
print(kod.shape[1]) #column
print(kod.shape[0]) #row


len(kod)

print(kod[:,::2]) #even columns   :2 ----step size
print(kod[:,1::2]) #odd columns
