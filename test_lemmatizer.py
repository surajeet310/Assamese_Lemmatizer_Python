import io
from Assamese_Stopwords import stopWord_assamese
import testExc as tE


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
        self.notFound = []
        self.counter = 0
 
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
 
    def searchItems(self,word):
        if(self.searchExceptionalWords(word)):
            w = self.searchExceptionalWords(word)
            return w
        currentNode = self.rootNode
        found = False
        data =[]
        for i in range(len(word)):
            ch=word[i]
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
            lemma = self.remove2nd(word)
            if lemma is not None:
                return lemma
            else:
                self.notFound.append(word)
                return ''
    
    def remove2nd(self,word):
        old = list(word)
        if(len(old)>=3):
            redunt = old[1]
            old.remove(redunt)
            new = ''.join(old)
            curr = self.rootNode
            lemma=[]
            for j in range(len(new)):
                c = new[j]
                if c in curr.childNode:
                    curr = curr.childNode[c]
                    lemma.append(c)
                else:
                    if(j==0):
                        break
                    elif(curr.checkEndOfWord()):
                        break
                    else:
                        continue
            if(curr.checkEndOfWord()):
                return ''.join(lemma)
            else:
                return None
        else:
            return None



    def searchExceptionalWords(self,word):
        exc = dict()
        otherForms=[]
        root=[]
        with open("exceptional.txt","r") as f1:
            otherForms = f1.read().split()
        with open("exceptionalRoot.txt","r") as f2:
            root = f2.read().split()
        
        for i in range(len(otherForms)):
            item1 = otherForms[i]
            item2 = root[i]
            exc[item1]=item2
        
        if word in exc:
            temp=exc[word]
            return temp
        else:
            return False
    
        

def getInput(inputString):
    TrieObj = Trie_struct_operations()
    StopWordsObj = stopWord_assamese()
    tokenized_words = []
    lemmaList = []
    wordList = []
    inflected_root = dict()
    with open("aL.txt","r") as file:
        wordList = file.read().split()
    
    TrieObj.addWords(wordList)
    
    input_str = inputString
    tokens = input_str.split()

    for t in tokens:
        tokenized_words.append(t)
    
    
    for w in tokenized_words:
        res = StopWordsObj.search(w)
        if(res):
            tokenized_words.remove(w)
    for word in range(len(tokenized_words)):
        temp = TrieObj.searchItems(tokenized_words[word])
        inf = tokenized_words[word]
        if temp is not '':
            lemmaList.append(temp)
            inflected_root[inf] = temp
    
    notFoundWords = []
    newList=[]
    for nw in TrieObj.notFound:
        notFoundWords.append(nw)
    
    newDict = dict()
    newList,newDict = tE.getPrefixes(notFoundWords)
    
    for w in newList:
        lemmaList.append(w)
    
    word_root_f = open("words_root.txt","a")
    for items in inflected_root:
        word_root_f.write("{} - {}".format(items,inflected_root[items]))
        word_root_f.write("\n")
    for item in newDict:
        word_root_f.write("{} - {}".format(item,newDict[item]))
        word_root_f.write("\n")
    
    word_root_f.close()


    notfoundFile = open("notfoundData.txt","a")
    for nw in TrieObj.notFound:
        notfoundFile.write(nw)
        notfoundFile.write("\n")
    notfoundFile.close()
    return lemmaList



def getAccuracy(inputStr,lemmaList):
    token = inputStr.split()
    tokenList=[]
    StopObj = stopWord_assamese()
    for t in token:
        tokenList.append(t)
    for w in tokenList:
        r = StopObj.search(w)
        if(r):
            tokenList.remove(w)
    for i in lemmaList:
        if i == '':
            lemmaList.remove(i)
    
    acc = (len(lemmaList))/(len(tokenList))
    accPer = acc*100
    accPer = round(accPer,3)
    x=len(tokenList)
    y=len(lemmaList)
    outputlist=[]
    outputlist.append(x)
    outputlist.append(y)
    outputlist.append(accPer) 
    return outputlist   
    





        
    


        

        

