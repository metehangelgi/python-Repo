import numpy as np
import os

def f(s):
    return np.round(s/sum(s)*100, 2)

def met(file):
        lst = []
        for word in file:
            lower_case = word.lower()
            lst.append(lower_case)
        return lst




mete=["HGFRD"]


def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line


newmete=map(met,mete)
print_iterator(newmete)
print(mete)



meteh,an=os.path.splitdrive(os.getcwd())

print(meteh)
print(an)

#print(exec(open("Example_str_join.txt").read()))
