
#variables demonstrated
print("This program is a demo of variables")
v = 1
print("The value of v is now", v)
v = v + 1
print("v now equals itself plus one, making it worth", v)
v = 51
print("v can store any numerical value, to be used elsewhere.")
print("for example, in a sentence. v is now worth", v)
print("v times 5 equals", v*5)
print("but v still only remains", v)
print("to make v five times bigger, you would have to type v = v * 5")
v = v * 5
print("there you go, now v equals", v, "and not", v / 5)

#STRINGS
#giving variables text, and adding text.
word1 = "Good"
word2 = "Morning"
word3 = "to you too!"
print(word1, word2)
sentence = word1 + " " + word2 + " " +word3
print(sentence)

#STRINGS
cumle='bugun guzel bir gun'

# guess the output of the following and the type and see yourself, but first try to guess
cumle[3:5]

cumle[::2]

cumle='bu sabah hava guzel'
cumle

cumle[6]='h'   #ERR: Check this statement what kind of an error is this?
cumle=cumle[0:-6]+' cok '+cumle[-5:-1]
cumle_2=cumle[0:-6]+' cok '+cumle[-5:]

#Use a stride value of 2 to print out every second character of the string E ?

E='clocrkr1e1c1t'

#split returns a list of all the words in a string, or a list split on a specific character.
coursename='SELECTED TOPICS IN ENGINEERING INTRODUCTION TO PROGRAMMING FOR DATA SCIENCE ENGR 350'.split(' ')[0]
# [0] selects the first element of the list

#Make sure you convert objects to strings before concatenating.
#ERR 'ENGR 350'+2
'ENGR 350'+str(2)

#about types
print(type(""), type("x"), type(True), type(False))
#builtins.str, builtins.str, builtins.bool, builtins.bool


#LISTS
#Lists are a mutable data structure.
x=[1, 'a', 2, 'b']
type(x)

#Use append to append an object to a list.
x.append(3.3)
print(x)

#Use + to concatenate lists.
[1,2] + [3,4]

#Use * to repeat lists.
[1]*3

#Use the in operator to check if something is inside a list.
1 in [1, 2, 3]

#WHILE LOOP
a = 0
while a < 10:
    a = a + 1
    print(a)

#EXAMPLE
#Type this in, see what it does
x = 10
while x != 0:
    print("\n",x) #\n is newline
    x = x - 1
    print("wow, we've counted x down, and now it equals", x)
print("And now the loop has ended.")

#  if statement and example
#EXAMPLE 1
y = 1
if y == 1:
    print("y still equals 1, I was just checking")

#EXAMPLE 2
print("We will show the even numbers up to 20")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n)
    n = n + 1
print("there, done.")

# FOR LOOP
a=range(5)
for i in range(0,len(a)):print(' ',i,' - ',a[i])

b=range(3,300,3)
for i in range(0,len(b)): print(b[i])

#This is an example of how to loop through each item in the list.
# x is x=[1, 'a', 2, 'b']
for item in x:
    print(item)

#Or using the indexing operator:
i=0
while( i != len(x) ):
    print(x[i])
    i=i + 1

#INDENTATION
a = 10
while a > 0:
    print(a)
    if a > 5:
        print("Big number!")
    elif a % 2 != 0:
        print("This is an odd number")
        print("It isn't greater than five, either")
    else:
        print("this number isn't greater than 5")
        print("nor is it odd")
        print("feeling special?")
    a = a - 1
    print("we just made 'a' one less than what it was!")
    print("and unless a is not greater than 0, we'll do the loop again.")
print("well, it seems as if 'a' is now no bigger than 0!")
print("the loop is now over, and without furthur adue, so is this program!")

