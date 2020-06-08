# MONTHS
# As a TUPLE
months_tuple = (
'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
'  December')
print(months_tuple)
print(' - ' * 20)

# As a LIST
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', '  December']
print(months_list)
print(' - ' * 20)

# add a new value to the end of a list:
# list_name.append(value-to-add)
months_list.append('OnucuncuAy')
print(months_list)
print(' - ' * 20)

# delete a list element:
# del list_name[indice]
del months_list[4]
print(months_list)
print(' - ' * 20)

print('asdasdasda asda sda\taazxz\nz\r c\r\nx')

s = 'avbabvavb'
for item in s:
    print(item)
print(' - ' * 20)

for item in sorted(s):
    print(item)
print(' - ' * 20)

for item in set(s):
    print(item)
print(' - ' * 20)

for item in reversed(s):
    print(item)
print(' - ' * 20)

for item in set(s).difference(t):
    print(item)
print(' - ' * 20)

t = 'b'
for item in set(s).difference(t):
    print(item)
print(' - ' * 20)
