import string
def avgLenSen(sentence:str) -> float:
    word_split = []
    word_len = 0
    punc = [',', '?', '!', '.', '\'']
    word_split = ''.join(filter(lambda x: x not in string.punctuation and  not x.isdigit()  and x !='', sentence)).split(' ')

    for word in word_split:
        #lambda x : word_split.remove(word) if x =='' else None
        word_len  += len(word.strip(''))

    total_len = len(word_split)
    print(word_split)
    return word_len / total_len

print(avgLenSen('hi amuktha.,\'123343'))

