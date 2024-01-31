import numpy as np

file_path = "/Users/stephenieoboh/Desktop/ENSF338/Lab1/pg2701.txt"

with open(file_path, 'r') as file:
    text = file.read()

lines = text.splitlines()
lines_array = np.array(lines)

start_counting = False
total_consonants = 0
total_words = 0

for line in lines_array:
    # Check if the line starts with the specified pattern
    if line.startswith("CHAPTER 1. Loomings."):
        start_counting = True
        continue

    # Start counting consonants when the pattern is found
    if start_counting:
        words = line.split()

        for word in words:
            consonants_count = sum(1 for char in word if char.isalpha() and char.lower() not in "aeiouy")

            total_consonants += consonants_count
            total_words += 1

average = total_consonants / total_words

# Print the result
print(f"Number of consonants: {total_consonants}")
print(f"Number of words: {total_words}")
print(f"Average number of consonants per word: {average}")
