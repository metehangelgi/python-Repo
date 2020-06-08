
# Python program to demonstrate working# of 
# Set in Python 
  
# Creating two sets 
set1 = set() 
set2 = set() 
  
# Adding elements to set1 
for i in range(1, 6): 
    set1.add(i) 
  
# Adding elements to set2
for i in range(3, 8): 
    set2.add(i) 
  
print("Set1 = ", set1) 
print("Set2 = ", set2) 
print("\n") 
  
# Union of set1 and set2 
set3 = set1 | set2    # set1.union(set2) 
print("Union of Set1 & Set2: Set3 = ", set3) 
  
# Intersection of set1 and set2 
set4 = set1 & set2    # set1.intersection(set2) 
print("Intersection of Set1 & Set2: Set4 = ", set4) 
print("\n") 
  
# Checking relation between set3 and set4 
if set3 > set4:      # set3.issuperset(set4) 
    print("Set3 is superset of Set4") 
elif set3 < set4:    # set3.issubset(set4) 
    print("Set3 is subset of Set4") 
else : # set3 == set4 
    print("Set3 is same as Set4") 
  
# displaying relation between set4 and set3 
if set4 < set3:    # set4.issubset(set3) 
    print("Set4 is subset of Set3") 
    print("\n") 
  
# difference between set3 and set4 
set5 = set3 - set4 
print("Elements in Set3 and not in Set4: Set5 = ", set5) 
print("\n") 
  
# checkv if set4 and set5 are disjoint sets 
if set4.isdisjoint(set5): 
    print("Set4 and Set5 have nothing in common\n") 
  
# Removing all the values of set5 
set5.clear() 
  
print("After applying clear on sets Set5: ") 
print("Set5 = ", set5) 



>>> thisset = {"elma", "muz", "kiraz"}
>>> thisset
{'elma', 'kiraz', 'muz'}
>>> thisset.update(["erik", "mango", "portakal"])
>>> thisset
{'erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'}
>>> thisset.update(["erik", "mango", "portakal"])
>>> thisset
{'erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'}
>>> print(thisset)
{'erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'}
>>> thisset.discard("muz")
>>> print(thisset)
{'erik', 'elma', 'mango', 'kiraz', 'portakal'}
>>> thisset.pop()
'erik'
>>> print(thisset)
{'elma', 'mango', 'kiraz', 'portakal'}
>>> a=set(('erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'))
>>> a
{'erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'}
>>> a.difference(thisset)
{'erik', 'muz'}
>>> thisset.difference(a)
set()
>>> a.difference_update(thisset)
>>> a
{'erik', 'muz'}
>>> thisset
{'elma', 'mango', 'kiraz', 'portakal'}
>>> thisset.difference_update(a)
>>> thisset
{'elma', 'mango', 'kiraz', 'portakal'}
>>> a
{'erik', 'muz'}
>>> a=set(('erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'))
>>> thisset.difference_update(a)
>>> a
{'erik', 'muz', 'elma', 'mango', 'kiraz', 'portakal'}
>>> thisset
set()
>>> a.isdisjoint(thisset)
True
# Return a set that contains all items from both sets, except items that are present in both sets:
# Meaning: The returned set contains a mix of items that are not present in both sets.

>>> x = {"elma", "muz", "kiraz"}
>>> y = {"google", "microsoft", "elma"}
>>> z = x.symmetric_difference(y)
>>> x
{'elma', 'kiraz', 'muz'}
>>> y
{'elma', 'google', 'microsoft'}
>>> z
{'muz', 'google', 'microsoft', 'kiraz'}
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
>>> x
{'elma', 'kiraz', 'muz'}
>>> y
{'elma', 'google', 'microsoft'}
>>> x.symmetric_difference_update(y)
>>> x
{'google', 'muz', 'microsoft', 'kiraz'}
>>> y
{'elma', 'google', 'microsoft'}
