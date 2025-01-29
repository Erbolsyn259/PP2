def generate_permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return
    
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        generate_permutations(remaining, current + s[i])

def print_permutations():
    user_input = input("Введите строку: ")
    generate_permutations(user_input)

print_permutations()