from pyiwn import pyiwn

#pyiwn.langs()
#pyiwn.download()

iwn = pyiwn.IndoWordNet('assamese')
word_list = iwn.all_words()

file_buffer = open("ALemma.txt","a")
for w in range(len(word_list)):
    file_buffer.write(word_list[w])
    file_buffer.write("\n")

file_buffer.close()
