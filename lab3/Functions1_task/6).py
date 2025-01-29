def reverse_words():
    user_input = input("Enter a sentence: ")
    
    reversed_sentence = ' '.join(user_input.split()[::-1])
    
    return reversed_sentence

result = reverse_words()
print(result)
