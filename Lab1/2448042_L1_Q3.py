# Q3. Regular Expression 
# 2.1. Write regular expressions for the following languages :

import re

# 1) the set of all alphabetic strings 

pattern1 = r'^[A-Za-z]+$'
test_strings1 = ["Hello", "Python3", "duma", "123", "DUMA"]
print("\nAlphabetic strings only :")
for string in test_strings1:
    if re.fullmatch(pattern1, string):
        print(f"'{string}' is valid")
    else:
        print(f"'{string}' is not valid")
        

# 2)  the set of all lower case alphabetic strings ending in a b

pattern2 = r'^[a-z]*b$' 
test_strings2 = ["ab", "cab", "bb", "hello", "aaB", "b", "xyzb"]
print("\nLowercase alphabetic strings ending in 'b'")
for string in test_strings2:
    if re.fullmatch(pattern2, string):
        print(f"'{string}' is valid")
    else:
        print(f"'{string}' is not valid")
        

# 3) the set of all strings from the alphabet a,b such that each a is immediately preceded by and immediately followed by a b

pattern3 = r'^(b*(ab)+b*)*$'  # every 'a' must be between 'b's

test_strings3 = ["bab", "bbabb", "ab", "a", "baba", "b", "aa", "bb"]
print("\nEach 'a' must be immediately preceded and followed by 'b'")
for string in test_strings3:
    if re.fullmatch(pattern3, string):
        print(f"'{string}' is valid")
    else:
        print(f"'{string}' is not valid")
        


# 2.2. Write regular expressions for the following languages. By “word”, we mean an alphabetic string separated from other words by whitespace, any relevant
# punctuation, line breaks, and so forth.
# 1. the set of all strings with two consecutive repeated words (e.g., “Humbert Humbert” and “the the” but not “the bug” or “the big bug”);
# 2. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;
# 3. all strings that have both the word grotto and the word raven in them (but not, e.g., words like grottos that merely contain the word grotto);
# 4. write a pattern that places the first word of an English sentence in a register. Deal with punctuation.


# Q1: Two consecutive repeated words
print("Repeated words")
test_sentences1 = [
    "Humbert Humbert loved Lolita.",
    "the the dog barked",
    "the big bug",
    "go go go",
    "hello Hello"
]
pattern1 = r'\b(\w+)\s+\1\b'
for sentence in test_sentences1:
    match = re.search(pattern1, sentence, re.IGNORECASE)
    if match:
        print(f"Match: '{match.group()}' in → '{sentence}'")
    else:
        print(f"No match → '{sentence}'")

# Q2: Start with integer and end with word
print("\nStarts with integer and ends with word")
test_sentences2 = [
    "123 the",
    "4567 hello there",
    "98 Done!",
    "Start 123",
    "12"
]
pattern2 = r'^\d+.*\b[a-zA-Z]+\b$'
for sentence in test_sentences2:
    match = re.fullmatch(pattern2, sentence)
    if match:
        print(f"Valid → '{sentence}'")
    else:
        print(f"Invalid → '{sentence}'")

# Q3: Contains both 'grotto' and 'raven'
print("\nContains both 'grotto' and 'raven'")
test_sentences3 = [
    "The raven sat outside the dark grotto.",
    "There was a grotto raven but no raven here.",
    "Ravens flew past grottos.",
    "The grotto had nothing in it.",
    "grotto raven"
]
pattern3 = r'\b(?=.*\bgrotto\b)(?=.*\braven\b).*'
for sentence in test_sentences3:
    match = re.search(pattern3, sentence, re.IGNORECASE)
    if match:
        print(f"Valid → '{sentence}'")
    else:
        print(f"Invalid → '{sentence}'")

# Q4: First word of the sentence
print("\nFirst word of sentence")
test_sentences4 = [
    " Hello, how are you?",
    "Start the machine.",
    "  wait! I’ll do it.",
    "123 Go",
    "?Who knows."
]
pattern4 = r'^\s*([A-Za-z]+)\b'
for sentence in test_sentences4:
    match = re.match(pattern4, sentence)
    if match:
        print(f"First word: '{match.group(1)}' from → '{sentence}'")
    else:
        print(f"No first word found → '{sentence}'")
