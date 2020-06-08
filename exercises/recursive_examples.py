def fact(n:int):
    if n == 0:
        return 1
    return n*fact(n-1)

def prod(int_iter):
    p = 1
    for x in int_iter:
        p *= x
    return p

def fact_prod(n):
    return prod(range(1, n+1))


def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)



