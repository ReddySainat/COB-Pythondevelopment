import string

# Function to count unique words and their occurrences in a text
def count_unique_words(text):
    word_count = {}
    
    # Remove punctuation, convert to lowercase, and split text into words
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Main program
if _name_ == "_main_":
    # Replace this with your own text or sentence
    text = "im from siddharth institution of engineering and technology my self sainath"

    unique_word_count = count_unique_words(text)
    
    print("Unique words and their occurrences:")
    for word, count in unique_word_count.items():
        print(f"{word}: {count}")
