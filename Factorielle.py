def factoriell(n):
    if type(n) != type(int):
        print("error type")
    if n<0 :
        print("value error, cannot be negative")
    if n==0 or n==1 :
        return 1
    if n>1:
        return n*factoriell(n-1)