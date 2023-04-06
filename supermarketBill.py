from datetime import datetime
name=input("Enter Your Name : ")

list='''------------------------------------
|S.No. |  Items     |  Prices      |
|------|------------|--------------| 
|1.    |  Sugar     |  Rs 40/Kg    |
|2.    |  TeaPowder |  Rs 200/Kg   | 
|3.    |  Salt      |  Rs 30/Kg    |
|4.    |  ToothPast |  Rs 20/Item  |
------------------------------------'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={"sugar":40,"teapowder":200,"salt":30,"toothpast":20,"rice":25}

print(list)
for i in range(len(items)):

   num=int(input(("if you want to Continue Shoping press 1 or Exit press 2 :")))    
   if num==1:
    item=input("Please Type Your Iteam Name : ").lower()
    quantity=float(input("Please Type Your Iteam Quantity : "))
    if item in items.keys():
        price=quantity*(items[item])
        pricelist.append((item,quantity,items,price))
        totalprice+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalprice*5)/100
        finalAmount=totalprice+gst
    else:
        print("You are Entered Iteam is Out of Stock")
    inpt=input("Can i Bill the Items y/n : ").lower()
    if inpt=="y":
      
      if finalAmount!=0:
        for i in range(len(pricelist)):
            print(25*"=","Miniki Super Market","="*25)
            print(28*" ","Hyderabad")
            print("Name : ",name," "*30,"Date",datetime.now())
            print("-"*75)
            print("S.No.",10*" ","iteams",10*" ","Quntitey",6*" ","price")
            for i in range(len(pricelist)):
                print(i+1,10*" ",4*" ",ilist[i],11*" ",qlist[i],13*" ",plist[i])
            print("-"*75)
            print(50*" ","Total Amount : ","Rs",totalprice)
            print(50*" ","GST Amount   : ","Rs",gst)
            print(50*" ","Final Amount : ","Rs",finalAmount)
            print(75*"-")
            print(50*" ","Thanking You Visit Again")
            print(75*"-")
            print(i,ilist[i],qlist[i],plist[i])
   elif num==2:
    print("**************Thanking You Visit Again**************")
    break
   else:
    print("Yor are Entered Invalid Number So We are Exiting")
    print("**************Thanking You Visit Again**************")
    break

