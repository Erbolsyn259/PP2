import time 
import math

try:
    def func(number,micsecond):
        second= micsecond /1000.0

        time.sleep(second)

        root = math.sqrt(number)

        print(f"Square root of {number} after {micsecond} miliseconds is {root}")

    num = int(input("enter your number"))

    mic = int(input("enter your microsecond"))

    func(num,mic)
except:
    print("Error")