# File        :   vowels.py
# Version     :   1.0.1
# Description :   Solution to the vowel counting problem
#
# Date:       :   Jan 04, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

# Requirement:
# Write a program that count how many times each vowel appears in an
# input word.

# List of vowels:
vowels = ("a", "e", "i", "o", "u")

# dict initialization:
counter = {}
for vowel in vowels:
    counter[vowel] = 0

# input prompt:
inputWord = input("Input word: ")

# vowel counting:
lineBuffer = ""
for letter in inputWord:
    # if letter in dict, increment frequency:
    if letter in counter:
        counter[letter] += 1
        vowelChar = letter
    else:
        vowelChar = "-"

    # Create vowel location diagram:
    lineBuffer += vowelChar

# print input word:
print(inputWord)
# print vowel location:
print(lineBuffer)

# print counter
print(counter)
