# Practice Q1. Text Normalization
# Perform EDA operation for the text file containing a chapter of a text book or story book.

import string
from collections import Counter

# Step 1: Load the file
with open("2448042_L1_Chapter.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()        
    file.seek(0)
    raw_text = file.read()          

# Step 2: Basic statistics
num_lines = len(lines)
num_chars = len(raw_text)

# Step 3: Text normalization
text_lower = raw_text.lower()
text_no_punct = text_lower.translate(str.maketrans("", "", string.punctuation))
words = text_no_punct.split()

# Step 4: Word statistics
total_words = len(words)
unique_words = len(set(words))
word_freq = Counter(words)
most_common = word_freq.most_common(10)
least_common = word_freq.most_common()[-10:]
longest_word = max(words, key=len)

# Step 5: Print all EDA results
print("---- Text EDA Report ----")
print(f"Total Lines: {num_lines}")
print(f"Total Characters: {num_chars}")
print(f"Total Words: {total_words}")
print(f"Unique Words: {unique_words}")
print(f"Longest Word: {longest_word}")

print("\nTop 10 Most Frequent Words:")
for word, count in most_common:
    print(f"{word}: {count}")

print("\n10 Least Frequent Words:")
for word, count in least_common:
    print(f"{word}: {count}")
