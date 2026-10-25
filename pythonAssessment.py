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

# print(f"The most common word is '{identify_most_common_word(content)}'.")

def calculate_average_word_length(text):
    if not text:
        return 0

    words = text.split()
    total_characters = 0
    word_count = 0
    for word in words:
        word = word.strip(string.punctuation + "“”‘’")

        if len(word) > 0:
            total_characters += len(word)
            word_count += 1

    if word_count > 0:
        average_length = total_characters / word_count
    else:
        average_length = 0
    return average_length

# print(f"The average word length is {calculate_average_word_length(content):.2f} characters.")


def count_paragraphs(text):
    if not text:
        return 1

    paragraphs = text.split("\n\n")
    count = 0
    index = 0

    while index < len(paragraphs):
        paragraph = paragraphs[index]
        if paragraph.strip():
            count += 1
        index += 1

    return count

print(f"The article has {count_paragraphs(content)} paragraphs.")