# Q2. Text Processing (Basics)

# Importing the required libraries
import nltk
from collections import Counter
nltk.download('punkt_tab')      # Downloading the 'punkt_tab' module

# a)  Define a string containing a paragraph as the value.
paragraph = """A bright, sunny day is a welcome sight, filling the world with warmth and light. 
The sky is a brilliant blue, and white, fluffy clouds drift lazily across the expanse, casting a gentle shadow here and there. 
The sun shines warmly, and the air feels fresh and clean, carrying the scent of blooming flowers and the sound of chirping birds."""

lower_paragraph = paragraph.lower()     # Converting the paragraph into lowercase
tokens = nltk.word_tokenize(lower_paragraph)        # Tokenizing the paragraph into words
words = [word for word in tokens if word.isalpha()]     # Filtering out the punctuations and keeping only the alphabetic words

# b) Write a program to print the number of total words and total unique words in the paragraph.

# Number of total words in the paragraph
total_words = len(words)
print("The total number of words in the paragraph is :", total_words)

# Number of unique words in the paragraph
unique_words = len(set(words))
print("The number of unique words in the paragraph is :", unique_words)


# c) Find the frequency of all words and also display the most and least frequent word.

# Frequency of all words 
word_frequencies = Counter(words)
print("\n Word Frequencies :")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq}")

# Most frequent word
most_frequent = word_frequencies.most_common(1)[0]
print("The most frequent word in the paragraph is :")
print(f"{most_frequent[0]} : {most_frequent[1]} times")

# Least frequent word
least_frequent = min(word_frequencies.items(), key=lambda item: item[1])
print("\nLeast Frequent Word:")
print(f"{least_frequent[0]}: {least_frequent[1]} time")


# d) Find the longest word in the paragraph.
longest_word = max(words, key=len)
print("\nLongest Word:")
print(longest_word)
