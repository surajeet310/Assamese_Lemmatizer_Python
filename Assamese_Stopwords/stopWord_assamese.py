
class stopWord_assamese:

    def __init__(self):
        self.found = False

    
    def search(self,word):
        
        file1 = open("stop_word_as_sample.txt","r")
        contents = file1.readlines()
        for x in range(50):
            wn = contents[x]
            l = len(word)
            for i in range(l):
                if(word[i] == wn[i]):
                    if((word[i] == wn[i]) & (i == l-1)):
                        self.found = True
                        return self.found
                    else:
                        continue
                else:
                    break
        
        

        
