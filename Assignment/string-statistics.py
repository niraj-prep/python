# String Statistics

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
num_vowels     = 0
num_consonants = 0
num_spaces     = 0
num_lowercase  = 0

for ch in string:
    if ch in vowels:
        num_vowels += 1
    elif ch.isalpha():
        num_consonants += 1
    if ch == " ":
        num_spaces += 1
    if ch.islower():
        num_lowercase += 1

print("\n--- String Statistics ---")
print("a) Number of Vowels     :", num_vowels)
print("b) Number of Consonants :", num_consonants)
print("c) Number of Spaces     :", num_spaces)
print("d) Number of Lowercase  :", num_lowercase)