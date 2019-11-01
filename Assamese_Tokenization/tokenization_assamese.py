
class tokenization_assamese:


    def __init__(self):
        self.word_list = []

    def word_tokenize(self,sentence):
        word = ''
        lengthOfSentence = len(sentence)
        for i in range(lengthOfSentence):
            ch = sentence[i]
            if(ch == ' '):
                self.word_list.append(word)
                word = ''
                continue
            else:
                word+=ch
    
    def get_tokenized_words(self):
        return self.word_list



    