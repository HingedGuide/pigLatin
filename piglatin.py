def pigLatinSentence(sentence):
    words = sentence.split()
    sentence = ""
    for word in words:
        if word[0] in ["a","e","i","o","u"]:
            word += 'way'
            sentence += word + ' '
        else:
            to_be_added = ''
            letter_index = 0
            while word[letter_index] not in ["a","e","i","o","u"]:
                to_be_added += word[letter_index]
                letter_index += 1
            to_be_added += 'ay'
            sentence += to_be_added + ' '
    return sentence

test1 = 'alfred'
test2 = 'wall street journal'

print(pigLatinSentence(test2))