def match_words(words):
    ctr = 0
    lst = []
    for w in words:
        if len(w) > 1 and w[0] == w[-1]:
            ctr += 1
            lst.append(w)

    print("list of words with first and last chacter same") 
    print(lst)
    return ctr

word_list = ['abc', 'cfc', 'xyz', 'aba', '1221']
count = match_words(word_list)
print("number of words having first and last character same:", count)
