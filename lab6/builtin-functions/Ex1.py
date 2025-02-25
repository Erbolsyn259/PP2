from functools import reduce
import operator

try:
    def mul(x):
        return reduce(operator.mul,x,1)

    list = [2,3,4,5,6,3,2]

    print(mul(list))
except:
    print("Error")