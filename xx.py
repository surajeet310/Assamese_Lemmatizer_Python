import io


class Trie_Node_Struct(object):
     
    def __init__(self):
        self.childNode = dict()
        self.endOfWord = False
    
    def setEndOfWord(self,val):
        self.endOfWord = True
    
    def checkEndOfWord(self):
        return self.endOfWord
 
 
class Trie_struct_operations(object):
 
    def __init__(self):
        self.rootNode = self.getNode()
        self.words = []
        
    def getNode(self):
        return Trie_Node_Struct()
    
    def addWords(self,wordList):
        for w in wordList:
            self.addItems(w)
 
    def addItems(self,word):
        currentNode = self.rootNode
        for i in range(len(word)):
            ch = word[i]
            if ch not in currentNode.childNode:
                currentNode.childNode[ch] = self.getNode()
            currentNode = currentNode.childNode[ch]
        currentNode.setEndOfWord(True)
    
    def search(self,new):
        currentNode = self.rootNode
        data=[]
        for i in range(len(new)):
            ch=new[i]
            if ch in currentNode.childNode:
                currentNode = currentNode.childNode[ch]
                data.append(ch)
            else:
                if(i==0):
                    break
                elif(currentNode.checkEndOfWord()):
                    break
                else:
                    continue
        found = currentNode.checkEndOfWord()
    
        if(found):
            return ''.join(data)
        else:
            return ''





    def s2(self,word):
        word1 = list(word)
        word2=[]
        lemma=''
        length = len(word1)
        sp_ch = word1[length-1]
        word2.append(word1[0])
        word2.append(sp_ch)
        for i in range(1,length):
            word2.append(word1[i])
        
        new = ''.join(word2)
        lemma=self.search(new)
        if lemma is not '':
            return lemma
        else:
            extr = self.s3(word)
            if extr is not '':
                nnextr = self.search(extr)
                if nnextr is not '':
                    return nnextr
                else:
                    return ''
            
            else:
                return ''
        
    def s3(self,word):
        w1 = list(word)
        temp = word[1]
        del(w1[1:2])
        w1.append(temp)
        return ''.join(w1)
    
    def s4(self,word):
        word1 = list(word)
        word2=[]
        lemma=''
        length = len(word1)
        sp_ch = word1[length-1]
        word2.append(word1[0])
        word2.append(word1[1])
        word2.append(sp_ch)
        for i in range(2,length):
            word2.append(word1[i])
        
        new = ''.join(word2)
        lemma = self.search(new)
        if lemma is not '':
            return lemma
        else:
            return ''





def getPrefix(notFoundList):
    TrieObj = Trie_struct_operations()
    tokenized_words = []
    lemmaList = []
    wordList = []
    with open("testdata.txt","r") as file:
        wordList = file.read().split()
    
    TrieObj.addWords(wordList)
    tokenized_words = notFoundList

    for t in tokenized_words:
        lemma = TrieObj.s2(t)
        if lemma is not '':
            lemmaList.append(lemma)
            tokenized_words.remove(t)
    
    for t in tokenized_words:
        newLemma = TrieObj.s4(t)
        if newLemma is not '':
            lemmaList.append(newLemma)
    
    
    return lemmaList




    
    
    
    


        


        

        

