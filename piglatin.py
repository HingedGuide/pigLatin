def convert_to_pig_latin(sentence):
    def convert_word(word):
        vowels = 'aeiou'
        if word[0] in vowels:
            return word + 'way'
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    return word[i:] + word[:i] + 'ay'
            return word + 'ay'  # In case there are no vowels in the word, not common but just in case.

    return ' '.join(convert_word(word) for word in sentence.split())


# Example usage
sentence = "this is pig latin"
pig_latin_sentence = convert_to_pig_latin(sentence)
print(pig_latin_sentence)  # isthay isway igpay atinlay
