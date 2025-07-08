# Practice Q2. From TextBook Exercises: Steve Bird and team

import nltk 

# 24. Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].
# a. Ending in ize
# b. Containing the letter z
# c. Containing the sequence of letters pt
# d. Having all lowercase letters except for an initial capital (i.e., titlecase)

from nltk.book import text6

# Using set to avoid duplicates
words = set(text6)

# a. Words ending in 'ize'
ending_in_ize = [w for w in words if w.endswith('ize')]

# b. Words containing 'z'
containing_z = [w for w in words if 'z' in w]

# c. Words containing 'pt'
containing_pt = [w for w in words if 'pt' in w]

# d. Titlecase words (first letter capital, rest lowercase)
titlecase_words = [w for w in words if w.istitle()]

# Print results
print("a. Words ending in 'ize':")
print(ending_in_ize)

print("\nb. Words containing 'z':")
print(containing_z)

print("\nc. Words containing 'pt':")
print(containing_pt)

print("\nd. Titlecase words (Titlecase):")
print(titlecase_words)


# 25. Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:
# a. Print all words beginning with sh
# b. Print all words longer than four characters

# Defining the sentence
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# a. Printing all words beginning with 'sh'
words_starting_with_sh = [word for word in sent if word.startswith('sh')]
print("Words starting with 'sh':", words_starting_with_sh)

# b. Printing all words longer than 4 characters
words_longer_than_4 = [word for word in sent if len(word) > 4]
print("Words longer than 4 characters:", words_longer_than_4)


# 26. What does the following Python code do? sum(len(w) for w in text1) Can you use it to work out the average word length of a text?

# This is a generator expression that goes through each word w in text1 and calculates the length of each word using len(w) and adds up all those lengths using sum().
# We can use this generator expression to work out the average word length of a text. 

from nltk.book import text1
total_characters = sum(len(w) for w in text1)
total_words = len(text1)
average_word_length = total_characters / total_words
print("Average word length:", round(average_word_length, 2))


# 27. Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.

from nltk.book import text1

def vocab_size(text):
    return len(set(text))
print("Vocabulary size of text1:", vocab_size(text1))


# 28. Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.

from nltk.book import text1

def percent(word, text):
    return (text.count(word) / len(text)) * 100
result = percent("whale", text1)
print("Percentage of 'whale' in text1:", round(result, 2), "%")
