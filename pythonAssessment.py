import string

with open("News_Article_for_Python_Assessment.txt", "r", encoding="utf-8") as file:
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

get_word = input("Enter the word to search in article: ")
print(f"The word '{get_word}' appears {count_specific_word(content, "technology")} times ")