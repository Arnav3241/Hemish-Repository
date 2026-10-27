while True :
    d={'Book1':100,'Book2':90,'Book3':80,'Book4':70,'Book5':670,'Book6':50,'Book7':670}
    a=int(input("""Type 1 to add 3 books
Type 2 to delete a book
Type 3 to change price
Type 4 to show books with price greater than 400
Type 5 to show books with price lower than 200
Type 6 to get the MAX and MIN book prices: """))
    def addbook(x):
        for i in range(3):
            Bookii=input("Input the name of the book to be added : ")
            Priceii=int(input("Input the price of the book to be added : "))
            d.update({Bookii:Priceii})
        print(d)
    def remove(x):
        Booki=input("Input the name of the book to be removed : ")
        d.pop(Booki)
        print(d)
    def changeprice(x):
        Booki=input("Input the name of the book whose price is to be changed : ")
        Pricei=int(input("Input the new price of the book : "))
        if Booki in d:
            d.update({Booki:Pricei})
            print(d)
        else :
            print("Book Not Found!")
    def sort400(x):
        d1={}
        for i,v in d.items():
            if int(v)>400:
                d1.update({i:v})
        print(d1)
    def sort200(x):
        d2={}
        for i,v in d.items():
            if int(v)<200:
                d2.update({i:v})
        print(d2)
    def maxmin(x):
        MAX=max(list(d.values()))
        MIN=min(list(d.values()))
        for i,v in d.items():
            if v==MAX:
                print("Books along with their cost having Maximum Prices are: ",i,v)
        for i,v in d.items():       
            if v==MIN:
                print("Books along with their cost having Minimum Prices are: ",i,v)
    if a==1:
        addbook(1)
    elif a==2:
        remove(1)
    elif a==3:
        changeprice(1)
    elif a==4:
        sort400(1)
    elif a==5:
        sort200(1)
    elif a==6:
        maxmin(1)
    else :
        print("Tu Aan de aur Jaan de")
