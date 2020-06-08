

a=None

a==True
a==False
b=a

b==a


a=[1,2,'a','engr350',[1,5]]
len(a)
a[4][1]
a[1:4]
a[2:4]
mete=5
#a[4:1]  ---will have error


if mete==5:
    print("yes ı am")
elif mete==0:
    print("no ı am not ")




x,A=0,[]
L=[7,28,23,97,2,43,12,51,32,35,48,99]

for i in range(len(L)):
       if i%2==0:
           if L[i]%2==0:
               print(L[i])
               A.append(L[i])
               x+=1
for i in range(0,len(L),2):
    if L[i] % 2 == 0:
        print(L[i])
        A.append(L[i])
        x += 1


ahmet="metehan"
for i in L:
    print(i)






def mete(t):
    res=[]
    for s in t:
        res.append(s.capitalize())
    return res

def meteHızlı(t):
    return [s.capitalize() for s in t]


def uppers(t):
    res=[]
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def uppersHızlı(t):
    return [s for s in t if s.isupper()]




ahmet=mete(ahmet)
ahmet =meteHızlı(ahmet)
upperstest=uppers(ahmet)

print(ahmet)
print(upperstest)





ı,o,p=1,'a',True

print(ı==5)



print(ı==5 and o=='a',ı==1 or o=='a',p==True and o=='a')


metehan=[1,2,3]

sen=metehan

metehan.append(4)

print(sen)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.get("brand"))


del thisdict["brand"]
thisdict["mete"]="metehan"
thisdict["model"]="araba"

print(thisdict.get("brand"))



squares={ x: x*x for x in range(6)}
print(squares)



odd_sqr={x:x*x for x in range(11) if x%2==1}
print(odd_sqr)

#KAGEL
