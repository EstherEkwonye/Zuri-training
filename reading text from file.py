# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The meat is ready. It is a big meat!")


import re


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        contents = f.read()
        return contents
        f.close()


def count_words():
    text = read_file_content(".Zuri-training/story.txt")
    # [assignment] Add your code here
    words = text.split()
    word_count = {}
    for word in words:
        # filter punctuation and convert to lowercase
        word = re.sub(r'[^\w\s]', '', word).lower()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


print(count_words())