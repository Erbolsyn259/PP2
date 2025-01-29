import re

def is_palindrome(phrase):
    # Remove non-alphanumeric characters and convert to lowercase
    normalized_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase).lower()
    
    return normalized_phrase == normalized_phrase[::-1]

print(is_palindrome("madam"))      
print(is_palindrome("racecar"))        
print(is_palindrome("A man a plan a canal Panama")) 
print(is_palindrome("hello"))         
