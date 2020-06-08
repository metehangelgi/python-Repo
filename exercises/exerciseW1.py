

import  math







'''
    it is exercise 1-2 from Week1 
 written by Metehan Gelgi
 07.07.2019
'''



'''
exercises #1
A)
1-
a)it is waiting for finish my code(for forget second paranthesis)-invalid syntax
b)missing paranthesis error
2-interpreter think that i will continiue my string
3-gives 4 (2++2=4)----- (2+-2=0)----- (2+2=4)
4-SyntaxError: invalid token (4+001)
5-SyntaxError: invalid syntax (2 3)---- 2,4->(2, 4)


2-
a)(42*60  + 42)=2562
b)(10/1.61)=6.211180124223602
c)6.87 minutes 52.48 seconds


B)
1-
a-SyntaxError: can't assign to literal(24=n)
b-(x=y=3)  there is no error x and y set as 3
c-(x=5;) x set as 5
d-(xy)
    Traceback (most recent call last):
        File "<input>", line 1, in <module>
        NameError: name 'xy' is not defined

2-
a)math.pi*(r**3)
=392.6990816987241
b)
c)7.15.42






print(5++7)

list=[1,2,3,4,5]
myset={1,2,3,4}
tüp=(1,2,3,4)

for i in "mete":


'''




'''
exercises #2
'''

#1
fourth=int()
first=4/10 + 3.5*2
second=10%4 + 6/2
third=abs(4-20/3)**3
#fourth=math.sqrt(4.5-5)+7*3----> can not be done because we cannot take sqrt of negative numbers
fifth=3*10/3+10%3







print(type(first))
print(first)
print(type(second))
print(second)
print(type(third))
print(third)
print(type(fourth))
print(fourth)
print(type(fifth))
print(fifth)




#2

for i in range(5):
    print(i)




for i in range(3,10):
    print(i)



for i in range(4, 13 ,3):
    print(i)


for i in range(15, 5 ,-2):
    print(i)


for i in range(5,3): # did not print this one. so we have to expilicitly show when we want to range with reverse order
    print(i)




#3

''' a)
    alghorithm needs to be changed to the program to be executed
'''
''' b)
    Programming languages are (designed to be) easily used by machines, but not people.
Natural languages (like English) are easily used by humans, but not machines.
Programming languages are unambiguous, 
while natural languages are often multiply ambiguous and require interpretation in context to be fully understood 
    The vocabulary of natural languages is filled with conceptual terms. 
The vocabulary of programming languages is generally only ‘grammatical’/functional ‘words’ like basic comments, 
plus various custom-named things like variables and functions.


'''
'''
    c)
    A high-level language is a programming language that uses English and mathematical symbols, like +, -, % and many others, in its instructions.
When using the term 'programming languages,' most people are actually referring to high-level languages.
High-level languages are the languages most often used by programmers to write programs.
Examples of high-level languages are C++, Fortran, Java and Python.
    Machine language, or machine code, is the only language that is directly understood by the computer, and it does not need to be translated.
All instructions use binary notation and are written as a string of 1s and 0s. 
'''
'''
    e)
    The term syntax refers to grammatical structure 
    whereas the term semantics refers to the meaning of the vocabulary symbols arranged with that structure. 
'''


#5
print("it is 4th quiestion outcomes")
for i in range(1, 11):  #-> square of numbers
    print(i * i)

for i in [1,3,5,7,9]:  #->cube of numbers
    print(i, ":", i**3)
print(i)

x = 2
y = 10
for j in range(0, y, x): #increase 2 by 2
    print(j , x+y)
print("done")

ans = 0
for i in range(1, 11): # sum of squres 1-11
    ans = ans + i*i
    print(i)
print(ans)



h=int(input('hidrojen number >>>' ))
c=int(input('carbon number >>>'))
o=int(input('oksijen >>>'))


molekulWeight=(1.0079*h)+(12.011*c)+(15.9994*o)
print(molekulWeight)


#6


celsius=int(input('give my celcious >>>'))

fahrenheit=(9/5)*celsius+32

print("fahrenheit is: "+str(fahrenheit) )


#7



a=float(input('a is >>>'))
b=float(input('b is >>>'))
c=float(input('c is >>>'))


det=b*b-4*a*c

if det>0:

    quadratic1= (-b+math.sqrt(det))/(2*a)
    quadratic2 = (-b - math.sqrt(det)) / (2 * a)

else :
    quadratic = -b  / (2 * a)
    complexPart=math.sqrt(-det)/(2*a)
    quadratic2 = str(quadratic)+"+"+str(complexPart)+"i"
    quadratic1 = str(quadratic) + "-" + str(complexPart) + "i"



print("quadratic1->"+str(quadratic1))
print("quadratic1->"+str(quadratic2))


#8
r=float(input("enter the radious >>>"))


volume=4/3*math.pi*(r**3)
surfaceArea=4*math.pi*(r**2)


print(volume, surfaceArea)

#9

alan=math.pi*r**2
price=float(input("give price of per unit inch >>>"))
print(alan*price)


#10
speed=1100
time=float(input("give me time >>>"))


distance=time*speed

print(str(distance//5280)+" miles "+ str(distance% 5280)+" feets")



#11

pound=float(input("enter the weight as a pound"))


shipping=pound*0.86+1.5

price=shipping+10.50
print(price)


#12

n=int(input("enter the number of n"))

sum=0.0
for i in range(n):
    sum+=i
    print("sum of the first n natural numbers," , sum)

sum2=0.0
for i in range(n):
    sum2+=i*i
    print("sum of the squares for the first n natural numbers.", sum2 )

sum3=0.0
for i in range(n):
    number=float(input(str(i+1)+"th number >>>"))
    sum3+=number
    print("sum a series of numbers entered by the user", sum3)

sum4=0.0
for i in range(n):
    number=float(input(str(i+1)+"th number >>>"))
    sum4+=number
    average=float(sum4/n)
    print(" average of a series of numbers", average)


#13

side1=float(input("a side >>>"))
side2=float(input("b side >>>"))
side3=float(input("c side >>>"))

s=(a+b+c)/2

triangle=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle is", triangle)

#14

x1, y1=(int(x) for x in input("enter the coordinate 1 >>>").split())
x2, y2=(int(x) for x in input("enter the coordinate 2 >>>").split())

slope=(y2-y1)/(x2-x1)
print("slope of coordinates", slope)



#15
#coordinates are taken previous question

d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("distance between 2 coordinates is ",d)













