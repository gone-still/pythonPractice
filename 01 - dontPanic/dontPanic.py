# File        :   dontPanic.py
# Version     :   1.0.0
# Description :   Solution to the dontPanic problem
#
# Date:       :   Dec 31, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

# Requirement:
# Transform the string "Don’t panic!" into the string "on tap" using only the
# following list methods: pop, remove, insert, append

phrase = "Don't panic!"
plist = list(phrase)

# Characters to remove:
removeList = ["D", "'", "i", "c", "!", " "]

# Loop through the characters and remove targets:
for c in removeList:
    plist.remove(c)

# Pop last character (extra n):
plist.pop()

# Swap last and second to last:
swapChars = [plist.pop(), plist.pop()] # yields -> [a, p]
# Attach to original list (plist + [a, p]):
plist.extend(swapChars)

# Insert space at index 2:
plist.insert(2, " ")

# Join characters into string:
newPhrase = "".join(plist)
# Print the list & transformed string:
print(plist)
print(newPhrase)
