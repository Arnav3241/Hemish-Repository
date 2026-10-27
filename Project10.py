a=input("Give the name of file from where you want to count words from: ")
def linecount(file):
    with open(file,'rt+') as f:
        s=f.read()
        for i in s.splitlines():
            if len(i)>=50 and len(i.split())>7:
                print(i)
linecount(a)
