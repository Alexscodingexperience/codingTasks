# Get input from the user
str_manip = input("Enter a sentence: ")

str_manip_len = len(str_manip)
print(str_manip_len)

last_letter = str_manip[-1]

modified_input = ''.join('@' if char == last_letter else char for char in str_manip)
print(modified_input)

reversed_string = str_manip [-1:-4:-1]
print(reversed_string)

# Take the first 3 letters
first_three_letters = str_manip[:3]

# Take the last 2 letters
last_two_letters = str_manip[-2:]

# concatinate to create a new word
new_word = first_three_letters + last_two_letters

print(new_word)
