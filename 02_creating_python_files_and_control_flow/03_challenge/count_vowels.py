# ここにコードを書いてください
word = input('Enter a string:')
vowels = "aeiou"
number_of_vowels = 0

for letter in word.lower():
    for vowel in vowels:
        if letter == vowel:
            number_of_vowels += 1

print(f"Number of vowels:{number_of_vowels}")
