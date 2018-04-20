import numpy as np

def Fibonacci(a,b):
    v=np.arange(0,100)
    help1=a
    help2=b
    help3=str(a) + ' ' + str(b) + ' '
    for i in range(2,100):
        c=help1+help2
        help1=help2
        help2=c
        if i<99:
            help3+=str(c)+' '
        else:
            help3+=str(c)
    vege=help3.split(" ")
    print(vege)
    return 0



Fibonacci(0,1)