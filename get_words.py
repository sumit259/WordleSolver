def get_words():
    # Load the file.
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    return words
