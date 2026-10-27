a=input("Give the name of file from where you want to count words from: ")
word=input("Give the name of word to be counted: ")
def wordcount(file,word):
    with open(file,'rt+') as f:
        s=f.read()
        c=0
        for i in s.split():
            if i.lower()==word.lower():
                c+=1
        print("The number of occurences are : ",c)
wordcount(a,word)
        
        
