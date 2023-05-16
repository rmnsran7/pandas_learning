import random

nouns = ["dog", "cat", "house", "car", "book"]
verbs = ["run", "eat", "cry", "read", "sleep"]
adjs = ["happy", "sad", "big", "small", "brave", "funny"]
i = 0
while i < 30:
    zipped = list(zip(adjs, nouns, verbs))
    random.shuffle(zipped)
    random_sentence = zipped[0]

    sentence = " ".join(random_sentence)
    print(sentence)
    i += 1
