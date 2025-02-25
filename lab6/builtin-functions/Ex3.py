try:
    def polindrom(str):
        cleaned_str = ''.join(str.split()).lower()
        return cleaned_str == cleaned_str[::-1]

    strs = input("enter your polindrom")

    if polindrom(strs):
        print("Polindrom")
    else:
        print("is not polindrom")
except:
    print("Error")