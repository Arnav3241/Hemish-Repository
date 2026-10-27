a=input("Give the name of file from where you want to copy: ")
b=input("Give the name of file where you want to copy: ")
def alternate(file,NEW):
    with open(file,'rt+') as f:
        s=f.readlines()
    with open(NEW,'wt+') as n:
        c=1
        for i in s:
            if (c%2)==1:
                c+=1
                n.write(i.lower())
            else:
                c+=1
                n.write(i.upper())
alternate(a,b)
