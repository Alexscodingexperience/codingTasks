def alternate_case(input_string):
    result = ""
    to_upper = True  

    for char in input_string:
        if char.isalpha():  
            if to_upper:
                result += char.upper()
            else:
                result += char.lower()
            to_upper = not to_upper  
        else:
            result += char  

    return result

user_input = input("Enter a sentance: ")
result_string = alternate_case(user_input)
print("Result:", result_string)

def alternate_word_case(input_string):
    words = input_string.split()  

    
    result_words = [word.upper() if i % 2 == 0 else word.lower() for i, word in enumerate(words)]

    result_string = ' '.join(result_words)
    return result_string


user_input = input("Enter a sentance: ")
result_string = alternate_word_case(user_input)
print("Result:", result_string)
