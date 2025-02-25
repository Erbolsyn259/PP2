
try:
    def func(tpl):
        return all(tpl)

    tpls = (1,2,3,4,5)

    tpls2 = (1,2,0,3,4)

    print(func(tpls))

    print(func(tpls2))
except:
    print("Error")