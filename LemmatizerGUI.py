import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import test_lemmatizer as Al

class MainWindow(object):

    def __init__(self,rootFrame):
        self.accList=[]
        self.lemma = []
        self.rootFrame = rootFrame
        self.width = self.rootFrame.winfo_width()
        self.rootFrame.protocol("WM_DELETE_WINDOW",self.on_exit)
        self.tBox = tk.Entry(self.rootFrame)
        self.sButton = tk.Button(self.rootFrame,bg="grey",fg="white",text = 'Search Lemma', command = self.searchString)
        self.browswBtn = tk.Button(self.rootFrame, bg="grey",fg="white",text='Browse Files', command = self.browseFiles)
        self.head = tk.Label(self.rootFrame,text='Lemmatizer Tool',bg='white',padx=220,pady=20,fg='grey')
        self.head.place(x=0,y=0)
        self.head.configure(font=("Times New Roman",30))
    
    def on_exit(self):
        if messagebox.askokcancel("Quit","Are you sure you want to exit?"):
            self.rootFrame.destroy()
    
        
    def createTextBox(self):
        textBox = self.tBox
        textBox.place(x=200,y=122,width=270,height=28)
    
    def createButton(self):
        searchBtn = self.sButton
        searchBtn.place(x=480,y=120)
        browseBtn = self.browswBtn
        browseBtn.place(x=480,y=160)
    
    def getInputString(self):
        inputString = self.tBox.get()
        return inputString
    
    def searchString(self,inputStr=None):
        if inputStr == None:
            textStr = self.getInputString()
            if textStr is '':
                tk.messagebox.showinfo("Error","Enter a String first !")
                return
            self.lemma=Al.getInput(textStr)
            self.accList = Al.getAccuracy(textStr,self.lemma)
        else:
            self.lemma=Al.getInput(inputStr)
            self.accList = Al.getAccuracy(inputStr,self.lemma)
        output_frame = tk.Tk()
        output_frame.title("Output")
        output_frame.geometry("350x150")
        output_frame.grid()
        
        l2 = tk.Label(output_frame, text='Total number of input words are : {}'.format(self.accList[0]))
        l2.grid()
        l3 = tk.Label(output_frame, text='Total number of correctly lemmatized words are :{}'.format(self.accList[1]))
        l3.grid()
        l4 = tk.Label(output_frame, text='Total Accuracy Achieved is {}%'.format(self.accList[2]))
        l4.grid()
        # l1 = tk.Label(output_frame,text='The Required Lemma are : ')
        # l1.grid()
        
        # for i in range(len(self.lemma)):
        #     word = self.lemma[i]
        #     out_text = tk.Label(output_frame,text="{}".format(word))
        #     out_text.grid()
        
        close_btn_unsaved = tk.Button(output_frame, text="Don't Save and Exit", command = lambda: self.closeOutputWindow(output_frame))
        close_btn_unsaved.grid()

        close_btn_saved = tk.Button(output_frame, text="Save and Exit", command=lambda: self.saveOutput(output_frame,self.lemma))
        close_btn_saved.grid()


    def closeOutputWindow(self,op_frame):
        op_frame.destroy()
    
    def saveOutput(self,op_frame,lemmaList):
        file_extensions = [('All Files','*.*'),('Text Files','*.txt')]
        newfile_name = filedialog.asksaveasfilename(initialdir='/',filetypes=file_extensions,defaultextension=file_extensions)
        if newfile_name is None:
            op_frame.destroy()
        f1 = open(newfile_name,"a")
        for i in range(len(lemmaList)):
            f1.write(lemmaList[i])
            f1.write(" ")
        f1.close()
        tk.messagebox.showinfo("Alert","File Saved")
        op_frame.destroy()
    

    def browseFiles(self):
        wordList=[]
        file_ext = [('Text Files','*.txt')]
        fileName = filedialog.askopenfilename(initialdir='/',filetypes=file_ext,defaultextension=file_ext)
        if fileName is None:
            return
        with open(fileName,"r") as f2:
            wordList = f2.read().split()
       
        if FileNotFoundError:
            print("File Not Found")
        
        inputStr = " ".join(wordList)
        self.searchString(inputStr)
        
        f2.close()



def main():
    root = tk.Tk()
    root.title("Assamese Lemmatizer Tool")
    root.resizable(0,0)
    root.grid()
    root.geometry("700x400")
    mainW = MainWindow(root)
    mainW.createTextBox()
    mainW.createButton()
    root.mainloop()
        

if __name__ == "__main__": 
    main()