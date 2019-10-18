import io
import nltk
from nltk.tokenize import word_tokenize
from Assamese_Stopwords import stopWord_assamese


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
        currentNode = self.rootNode
        found = False
        data =[]
        for i in range(len(word)):
            ch=word[i]
            if ch in currentNode.childNode:
                currentNode = currentNode.childNode[ch]
                data.append(ch)
                if(currentNode.checkEndOfWord()):
                    found = True
                    break
                else:
                    continue
            else:
                found = False
                break
 
        if(found):
            return ''.join(data)
        else:
            return False



def main():
    TrieObj = Trie_struct_operations()
    StopWordsObj = stopWord_assamese()
    tokenized_words = []
    lemmaList = []
    wordList = []
    with open("aL.txt","r") as file:
        wordList = file.read().split()
    
    TrieObj.addWords(wordList)
    
    input_str = input("Enter Input String")
    tokens = word_tokenize(input_str)

    for t in tokens:
        tokenized_words.append(t)
    
    for w in tokenized_words:
        res = StopWordsObj.search(w)
        if(res):
            tokenized_words.remove(w)
    for word in range(len(tokenized_words)):
        temp = TrieObj.searchItems(tokenized_words[word])
        lemmaList.append(temp)
    
    print("The resultant Lemma from the input string are: ")
    print(lemmaList)

    output_file_write = open("Output.txt","a")
    for i in range(len(lemmaList)):
        output_file_write.write(lemmaList[i])
        output_file_write.write(" ")
    output_file_write.write("\n")
    output_file_write.close()



if __name__ == "__main__":
    main()

        
    


        

        

