import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import test_lemmatizer as Al

class MainWindow(object):

    def __init__(self,rootFrame):
        self.lemma = []
        self.rootFrame = rootFrame
        self.rootFrame.protocol("WM_DELETE_WINDOW",self.on_exit)
        self.ip_frame = tk.Frame(self.rootFrame)
        self.tBox = tk.Entry(self.ip_frame)
        self.sButton = tk.Button(self.ip_frame, text = 'Search Lemma', command = self.searchString)
        self.browswBtn = tk.Button(self.ip_frame, text='Browse Files', command = self.browseFiles)
    
    def on_exit(self):
        if messagebox.askokcancel("Quit","Are you sure you want to fuck off ?"):
            self.rootFrame.destroy()

    
    def createFrame(self):
        inputFrame = self.ip_frame
        inputFrame.grid()
        
    def createTextBox(self):
        textBox = self.tBox
        textBox.grid()
    
    def createButton(self):
        searchBtn = self.sButton
        searchBtn.grid()
        browseBtn = self.browswBtn
        browseBtn.grid()
    
    def getInputString(self):
        inputString = self.tBox.get()
        return inputString
    
    def searchString(self,inputStr=None):
        if inputStr == None:
            textStr = self.getInputString()
            self.lemma=Al.getInput(textStr)
        else:
            self.lemma=Al.getInput(inputStr)
        output_frame = tk.Tk()
        output_frame.title("Output")
        output_frame.geometry("350x150")
        output_frame.grid()
        l1 = tk.Label(output_frame,text='The Required Lemma are : ')
        l1.grid()
        for i in range(len(self.lemma)):
            word = self.lemma[i]
            label = tk.Label(output_frame,text='{}'.format(word))   
            label.grid() 
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
    mainW.createFrame()
    mainW.createTextBox()
    mainW.createButton()
    root.mainloop()
        

if __name__ == "__main__": 
    main()