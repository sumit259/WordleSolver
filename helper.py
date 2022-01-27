def matchesPattern(word, pattern):
    for pos in range(5):
        if pattern[pos] == '_':
            continue
        if word[pos] != pattern[pos]:
            return False
    return True


def missesPattern(word, pattern):
    for pos in range(5):
        if pattern[pos] == '_':
            continue
        if word[pos] == pattern[pos]:
            return False
    return True


def getWordsWithPattern(words, pattern):
    filtered = []
    for word in words:
        if matchesPattern(word, pattern):
            filtered.append(word)
    return filtered


def excludeWordsWithChars(words, chars):
    filtered = []
    for word in words:
        add = True
        for char in chars:
            if word[0] == char or word[1] == char or word[2] == char or word[3] == char or word[4] == char:
                add = False
                break
        if add:
            filtered.append(word)
    return filtered


def includeWordsWithChars(words, chars):
    filtered = []
    for word in words:
        add = True
        for char in chars:
            if word[0] != char and word[1] != char and word[2] != char and word[3] != char and word[4] != char:
                add = False
                break
        if add:
            filtered.append(word)
    return filtered


def getWordsExcludingPatterns(words, patterns):
    filtered = []
    for word in words:
        add = True
        for pattern in patterns:
            if not missesPattern(word, pattern):
                add = False
                break
        if add:
            filtered.append(word)
    return filtered
