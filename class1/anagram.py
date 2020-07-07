def anagram1(random_word):
    f = open("dictionary.words.txt", "r")
    dictionary={}
    words=f.read().split('\n')
    # print(len(words))
    for word in words:
        word=word.lower()
        s = ''.join(sorted(word))
        if s in dictionary:
            dictionary[s].append(word)
        else:
            dictionary[s]=[word]
    random=''.join(sorted(random_word))
    # print(dictionary.keys())
    if random in dictionary:
        return dictionary[random][0]
    return " "
print(anagram1('quaternary'))
