# Pig Latin Translator Project

'''Pig_latin function for converting english words in a sentence into latin'''
def pig_latin():
    sentence= input("Enter a Sentence: ")
    #Split the sentence using split()
    # Used string strip method to remove white spaces at the beginning and end of user input.
    while sentence != '':
        sentence_stripped = sentence.strip()
        new_sentence_arr = sentence_stripped.split(' ')
        new_sentence = []
        
        #Looping throgh the new_sentence to identify it meets all the requirements
        for word in new_sentence_arr:
            #If word begins with a vowel add "way" at the end.
            if word[0] in ["a", "e", "i", "o", "u"]:
                new_word = word + "way"
                new_sentence.append(new_word)

            #If word starts with another letter and is capital, take first letter put it at the end and add"ay".
            if word[0] not in ["a", "e", "i", "o", "u"]:
                
                if word[0].isupper():
                    new_word = word[1:] + word[0].lower() + "ay"
                    newword_capitalized = new_word[0].upper() + new_word[1:]
                    new_sentence.append(newword_capitalized)
                else:
                    new_word = word[1:] + word[0] + "ay"
                    new_sentence.append(new_word)
        # print(new_sentence)
        formed_sentence = ' '.join(new_sentence)
        print('pig_latin: {}'.format(formed_sentence))
        sentence= input("Enter a Sentence: ")
    print('function exit')                         
pig_latin()