while True :
    s=input("Give me a sentence :")
    v=0
    n=0
    c=0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
               v+=1
            else:
                c+=1
        elif ch.isnumeric():
            n+=1
    print(v,c,n)


    
