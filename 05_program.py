# Q7 (3 Marks): Write a function that takes a string and returns a new string with all vowels replaced by "*".

def replace_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result     


n = input("Enter the string:")
new = replace_vowels(n)
print(new)