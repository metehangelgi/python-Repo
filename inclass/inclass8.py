import numpy as np
import pandas as pd
import datetime
import time



'''
eski dosyaları okuma işlemini yap. Lazım görüyorsan

epoch-1970 1 january=t0

datetime:
    today()
    second(milisecond)<->date

time:



BASİC DATETİME.py koduna bak genelde 



'''




time.time()



#time.asctime([t])

time.localtime()

datetime.date(2019,7,30)


'''


-------------------------------------------------HW-----------------------------------------
you will ask birthday
calculate number of days until his birthday-- or check is it passed or will be come on that day.
-------------------------------------------------HW2-----------------------------------------
how many week in month?
first monday can be in week one or week 2 (calendar şekli pazartesiden başlar--basic_datetime.py codunda son basılan august bak.)
identify first monday of month(12)- calculate day of presentation day(every monday of the month-)

-------------------------------------------------HW3-----------------------------------------
worksheet2 for 
import *
import math
from math import pi
farkları -benzerlikleri?

-------------------------------------------------HW4-----------------------------------------+
get cvs from webpage-oxford cvs 
learn how to read from webpage
tmax- average for every 10 years(1910-1919:1920-1929...)
sun hours for 10 years where dos it start(you have to determine where does it start)



'''


'''
MODULES:
reliability: should check invalid inputs aas an example...



'''

'''
if __name== '__main__':
    main()


'''

import urllib.request

#wh=urllib.request('...')  # kodda sorun olabilir incele
#wh.read()




url='http://www.ku.edu.tr/'

sayfa=urllib.request.urlopen(url).read()
wf=open('mete.html','w')
sayfa_utf=sayfa.decode('utf-8')
type(sayfa_utf)

wf.write(sayfa_utf)
wf.close()

# bu kod hata verir çünkü bytes write yapılamaz string olmalıdır.
with urllib.request.urlopen('http://python.org/') as response:
    htmlPage=response.read()
type(htmlPage)



url2='https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt'

urllib.request.urlretrieve(url,filename='Oxford_wdata.txt')


'''
Numpy array kullanmak ile list kullanmak farkı nedir?

bunu bak sen dersten çıktıktan sonra işlendi..

x=[range(10)]
print(x)
[range(0, 10)]
print(x[0])
range(0, 10)
print(type(x[0]))
<class 'range'>
list(range(10))
Out[27]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



'''


