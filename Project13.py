a=input("Give the name of file from where you want to copy: ")
b=input("Give the name of file where you want to copy: ")
def remove(file,NEW):
    with open(file,'rt+') as f:
        s=f.readlines()
    with open(NEW,'wt+') as n:
        for i in s:
            i=i.capitalize()
            n.write(i)
        n.seek(0)
        p=n.read()
        while p.count("  ")>0:
            p=p.replace("  "," ")
        while p.count('\t')>0:
            p=p.replace('\t'," ")
        n.write(p)
        print(p)
remove(a,b)
