import io
<<<<<<< HEAD
=======
from Assamese_Stopwords import stopWord_assamese
>>>>>>> ad47fbd9bc6a9e8ebb4aba735d638beb923a5ab6


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
<<<<<<< HEAD
        self.words = []
        
=======
 
>>>>>>> ad47fbd9bc6a9e8ebb4aba735d638beb923a5ab6
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
 
<<<<<<< HEAD
                


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
=======
    def searchItems(self,word):
        currentNode = self.rootNode
        found = False
        data =[]
        for i in range(len(word)):
            ch=word[i]
            if ch in currentNode.childNode:
                currentNode = currentNode.childNode[ch]
                data.append(ch)
                
            else:
                found = False
                break
        found = currentNode.checkEndOfWord()
 
        if(found):
            return ''.join(data)
        else:
            x=self.searchDerivatives(word)
            if x is not None:
                return x
            else:
                return False
    
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
    

    def searchDerivatives(self,word):
        currentNode = self.rootNode
        found=False
        data=[]
        for c in range(len(word)):
            ch=word[c]
            if ch in currentNode.childNode:
                currentNode = currentNode.childNode[ch]
                data.append(ch)
            else:
                found = False
                pos = c
                newWord=self.removeChar(pos,word)
                self.searchDerivatives(newWord)
        found = currentNode.checkEndOfWord()
        if(found):
            return data
        else:
            return None

    def removeChar(self,position,word):
        charList = list(word)
        toRemove = word[position]
        charList.remove(toRemove)
        finalWord = ''.join(charList)
        print(finalWord)
        return finalWord

        




def main():
    TrieObj = Trie_struct_operations()
    StopWordsObj = stopWord_assamese()
    tokenized_words = []
    lemmaList = []
    wordList = []
    with open("aL.txt","r") as file:
        wordList = file.read().split()
    
    TrieObj.addWords(wordList)
    
    input_str = input("Enter Sentence")
    tokens = input_str.split()

    for t in tokens:
        tokenized_words.append(t)
    
    for w in tokenized_words:
        res = StopWordsObj.search(w)
        if(res):
            tokenized_words.remove(w)
    for word in range(len(tokenized_words)):
        temp = TrieObj.searchItems(tokenized_words[word])
        lemmaList.append(temp)
    
    #return lemmaList



    #print("The resultant Lemma from the input string are: ")
    print(lemmaList)


    """output_file_write = open("Output.txt","a")
    for i in range(len(lemmaList)):
        output_file_write.write(lemmaList[i])
        output_file_write.write(" ")
    output_file_write.write("\n")
    output_file_write.close()"""

if __name__ == '__main__':main()


>>>>>>> ad47fbd9bc6a9e8ebb4aba735d638beb923a5ab6


        
    


        

        

