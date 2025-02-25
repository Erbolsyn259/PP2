try:
    def counts(str):
        upper = 0
        lower = 0
        for char in str:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
        return upper,lower

    strs = input("enter your string")

    upper,lower = counts(strs)

    print(f"count lower = {lower}")
    print(f"count upper = {upper}")
except:
    print("Error")