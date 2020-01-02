import io

class Trie(object):

    def __init__(self):
        self.child = dict()
        self.eof = False
    
    def setEOF(self):
        self.eof = True
    
    def checkEOF(self):
        return self.eof


class TrieOP(object):

    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return Trie()
    
    def addLemma(self,words):
        for w in words:
            self.addWords(w)
    
    def addWords(self,word):
        current = self.root
        for w in word:
            if w not in current.child:
                current.child[w] = self.getNode()
            current = current.child[w]
        current.setEOF()
    
    def prefSearch(self,prefix):
        current = self.root
        data=[]
        for p in prefix:
            if p not in current.child:
                break
            data.append(p)
            current = current.child[p]
        
        
        
        if current.checkEOF():
            return ''.join(data)
        else:
            return ''
    






def main():
    
    T1 = TrieOP()
    words=[]
    tokenized=[]
    lemmas=[]
    with open("testdata.txt","r") as f:
        words = f.read().split()
    
    T1.addLemma(words)
    ipSentence = input("Enter sentence")
    tokenized = ipSentence.split()

    for word in tokenized:
        lemma = T1.prefSearch(word)
        if lemma is not '':
            lemmas.append(lemma)
    
    print(lemmas)


if __name__ == "__main__":
    main()


