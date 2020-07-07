def anagram2():
    f = open("dictionary.words.txt", "r")
    dictionary={}
    words=f.read().split('\n')
    # print(len(words))
    for word in words:
        word=word.lower()
        word_= word.replace("qu","q")
        s = ''.join(sorted(word_))
        if s in dictionary:
            dictionary[s].append(word)
        else:
            dictionary[s]=[word]
    return dictionary

random_word = "evstrvmywxziobwt"
substrings=[]
def substring(i,s):
    if i==len(random_word):
        substrings.append(s)
        return 0
    substring(i+1,s+random_word[i])
    substring(i+1,s)

def checkanagram(random_word,dictionary):
    l1=[1,1,2,1,1,2,1,2,1,3,3,2,2,1,1,2,3,1,1,1,1,2,2,3,2,3]
    random=''.join(sorted(random_word))
    point = 0
    if random in dictionary:
        for c in random:
            point += l1[ord(c)-97]
        return point, dictionary[random][0]
    return 0, ""

d=anagram2()
substring(0,"")
answer = ""
pointmax = 0
for s in substrings:
    p,q=checkanagram(s,d)
    if p>= pointmax:
        pointmax = p
        answer = q
print(answer)
