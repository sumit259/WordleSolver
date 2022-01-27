import random

import get_words
import helper
from config import *

if __name__ == '__main__':
    words = get_words.get_words()
    print("found " + str(len(words)) + " words:")
    # print(words)
    words = helper.getWordsWithPattern(words, PATTERN)
    print("found " + str(len(words)) + " words:")
    # print(words)
    words = helper.excludeWordsWithChars(words, EXCLUDE)
    print("found " + str(len(words)) + " words:")
    # print(words)
    words = helper.includeWordsWithChars(words, INCLUDE)
    print("found " + str(len(words)) + " words:")
    # print(words)
    words = helper.getWordsExcludingPatterns(words, MISPLACED)
    print("found " + str(len(words)) + " words:")
    print(words)
    print(random.choice(words))
