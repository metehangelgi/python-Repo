def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
# We can write this more concisely using a list comprehension:

def capitalize_all(t):
    return [s.capitalize() for s in t]

# List comprehensions can also be used for filtering. For example, this function selects only
# the elements of t that are upper case, and returns a new list:
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

# rewrite it using a list comprehension
def only_upper(t):
    return [s for s in t if s.isupper()]
