a=input("Give the name of file from where you want to count words from: ")
def printcount(file):
    with open(file,'rt+') as f:
        s=f.read()
        c=0
        for i in s.split():
            if 'sh' in i:
                c+=1
                print(i)
        print("The number of occurences of words containing 'sh' are : ",c)
printcount(a)

