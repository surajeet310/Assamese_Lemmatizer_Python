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
 
                


    def s2(self,word):
        current_node = self.rootNode
        data=[]
        for ch in word:
            if ch in current_node.childNode:
                current_node = current_node.childNode[ch]
                data.append(ch)
            else:
                continue
        strr = ''.join(data)
        if(strr == ''):
            return ''
        else:
            return strr
    


    def prefixRecur(self,node,pref):
        words = self.words
        if node.checkEndOfWord():
            words.append(pref)
        

        for w,n in node.childNode.items():
            self.prefixRecur(n,pref+w)
        
        
    def prefixSearch(self,word):
        current_node = self.rootNode
        data=[]
        for ch in word:
            if ch in current_node.childNode:
                data.append(ch)
                current_node=current_node.childNode[ch]
            else:
                break

        temp=''.join(data)
        self.prefixRecur(current_node,temp)
    

            

def getPrefixes(notFoundList):
    TrieObj = Trie_struct_operations()
    tokenized_words = []
    lemmaList = []
    wordList = []
    with open("testdata.txt","r") as file:
        wordList = file.read().split()
    
    TrieObj.addWords(wordList)
    tokenized_words = notFoundList
    new=dict()
    for x in tokenized_words:
        t1 = TrieObj.s2(x)
        if((t1 != '')&(len(t1)>=2)):
            TrieObj.prefixSearch(t1)
            new[x]=TrieObj.words
            TrieObj.words.clear()
    
    
    for keys in new:
        print("Inflected Word is {} and the list of possible lemma obtained are {}".format(keys,new[keys]))
        x=int(input("Select the prefered Lemma from the choices mentioned (starting from 0 onwards) or if none of them is the lemma then hit -1"))
        if(x!=-1):
            lemmaList.append(new[keys][x])
        else:
            continue
    
    for w in lemmaList:
        if w == '':
            lemmaList.remove(w)
    
    return lemmaList


        
    


        

        

