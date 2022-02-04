def myPow( x, n):
        if n == 1:
            return x
        else:
            return x * myPow(x,n-1)
print(myPow(99,999))