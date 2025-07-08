
# Q1. Installing NLTK, NLTK.book and practice the NLP Environment using the exercises :
# 1.  Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).
# 2.  Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form.
#     That works out to 141167095653376. How many hundred-letter strings are possible?

# Install nltk in the terminal using 'pip install nltk'

import nltk  # Importing the Natural Language Toolkit
nltk.download('book')   # Downloading the book module resources

from nltk.book import *     # Importing all the example texts and functions from the module book

# 1. Using Python Interpreter as a calculator
numerator = 12
denominator = (4 + 1)
result = numerator / denominator
print("The result of the arithmatic problem is :", result)

# 2. Combinatorics with Strings
alphabet_size = 26      
given_length = 10 
combination_10 = 26 ** 10
print("The total number of ten letter strings that can be formed from a 26 letter alphabet is :", combination_10)

required_length = 100
combination_100 = 26 ** 100
print("The number of 100 letter strings that can be formed from a 26 letter alphabet is :", combination_100)

