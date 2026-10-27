a=input("Give the name of file that is to be copied: ")
b=input("Give the name of file where it has to be copied: ")
def copyfiles(fileog,filenew):
    with open(fileog,'rt+') as f:
        s=f.readlines()
        fw=open(filenew,'wt+')
        for line in s:
            if line[0].lower() in 'aeiou' or line[0].isdigit():
                fw.write(line)
copyfiles(a,b)
