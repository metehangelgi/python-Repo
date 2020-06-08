"""
what does axis do in python
yatay(row için)->axis=1
düşey(coloumn için)->axis=0



"""
"""
sql tutorial check et:


SELECT * FROM [Customers]
where CustomerName like '%f%te'



SELECT ProductName FROM [Products]
where price<10



SELECT * FROM [Products]
where price<10
order by price desc



SELECT * FROM [Products]
where (price<10 and categoryid>5) or categoryid=5
order by price desc


SELECT * 
FROM [Products] p,categories c
where p.categoryid =c.categoryid
and c.categoryname='Beverages'
and price<15


SELECT * 
FROM [Orders] o,Customers c
where o.Customerid=c.customerid


SELECT * 
FROM [Orders] o,Customers c
where o.Customerid=c.customerid
and c.country='Argentina'


SELECT * 
FROM OrderDetails od,products p,categories c,suppliers s
where od.productid=p.productid
and c.categoryid=p.categoryid
and p.supplierid=s.supplierid
and c.categoryname='Seafood'

select * 
from categories, shippers

select c.categoryid a1,p.categoryid a2 
from categories c, products p


select firstname,count(*),count(orderid)
from orders o,employees e
where firstname='Janet'
and e.employeeid=o.employeeid


select firstname,count(*),count(orderid)
from orders o,employees e
where e.employeeid=o.employeeid
group by firstname

select CustomerName,count(*),count(orderid)
from orders o,customers c
where c.customerid=o.customerid
group by customername

select country,count(*),count(orderid)
from orders o,customers c
where c.customerid=o.customerid
group by country
order by count(orderid) desc

hangi ülkeden ne kadarlık sipariş verilmiş?
yerli müşteriler hangi yabancı tedarikçi ürünlerini satın almışlar?
bir ülkeden verilen en yüksek siparişler?,tutar ve adet olarak?
şekerleme  kategoriden verilen siparişlerin ülke ya da şehir bazında kırılımı?

"""

#import pysqlite3 as pylite3
import sqlite3 as lite




