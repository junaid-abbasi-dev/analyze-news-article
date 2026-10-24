import string
import math

with open("News_Article_for_Python_Assessment.txt", "r", encoding="utf-8-sig") as file:
    content = file.read()



def count_specific_word(text, word):

    count = 0
    words = text.split()
    word = word.lower()

    for item in words:
        item = item.lower().strip(string.punctuation + "“”‘’")
        if item == word:
            count += 1
    
    if count == 0:
        return 0
    else:
        return count

# get_word = input("Enter the word to search in article: ") 
# print(f"The word '{get_word}' appears {count_specific_word(content, get_word)} times.") 


def identify_most_common_word(text):
    if not text:
        return None


    word_counts = {}
    words = text.split()

    for word in words:
        word = word.lower().strip(string.punctuation + "“”‘’")
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    most_common = None
    highest_count = 0

    for key, value in word_counts.items():
        if value > highest_count:
            most_common = key
            highest_count = value

    return most_common

print(f"The most common word is '{identify_most_common_word(content)}'.")
