class FarmerNode:
    num_of_previous_items=0
    def __init__(self,name,FarmerId):
        self.name=name
        self.FarmerId=FarmerId
        self.items=[]
        self.weights=[]
        self.prices=[]
        self.num_of_previous_items=0
        self.earning=0
        self.security_num=0
        self.ref=None
        
    def inputData(self):
        num_of_items=(int(input("Enter the number of items you want to sell:")))
        if num_of_items!=0:
            print("Enter the items you want to sell:")
            for i in range(self.num_of_previous_items,self.num_of_previous_items+num_of_items):
                item=input()
                self.items.append(item)

            print("Enter the weight of items in kg, in the order in which the items have been inserted:")
            for i in range(self.num_of_previous_items,self.num_of_previous_items+num_of_items):
                weight=float(input())
                self.weights.append(weight)
                      
            print("Enter the price of items per kg, in the order in which the items have been inserted:")
            for i in range(self.num_of_previous_items,self.num_of_previous_items+num_of_items):
                price=int(input())
                self.prices.append(price)

            self.num_of_previous_items+=num_of_items
            print("Your earning is Rs.",self.earning)
            self.showData()
        else:
            print("Your earning is Rs.",self.earning)
            self.showData()

    def BuyItem(self):
        item_buying=input("Enter the item to be bought:")
        index=0
        for i in self.items:
            if i==item_buying:
                break
            index+=1
        weight_of_item=float(input("Enter weight of the item:"))
        if weight_of_item>self.weights[index]:
            print("Purchase not possible. Only ",self.weights[index],"kg of ",self.items[index]," is available\n")
        else:
            self.weights[index]-=weight_of_item
            cost=weight_of_item*self.prices[index]
            self.earning+=cost
            print("You have to pay Rs.",cost)
        self.showData()

    def showData(self):
        if self.num_of_previous_items==0:
            print("Store is Empty!!\n")
        else:
            print("Items in the store:")
            for i in range(0,self.num_of_previous_items):
                print(self.items[i],"  ",self.weights[i],"kg  Rs.",self.prices[i],"per kg")
            print()



class Farmer:
    f_id=0
    head=None
    
    def __init__(self):
        confirmation=input("You are into the Farmers' portal. Do you wish to continue?  y/n:")
        if confirmation=="y":
            self.inputChoice()
        elif confirmation=="n":
            return
        else:
            print("Wrong Choice")
        
    def inputChoice(self):
        ch=int(input("1)SignUp  2)Login  3)Leave the Database  4)Show Database:"))
        if ch==1:
            self.SignUp()
        elif ch==2:
            self.Login()
        elif ch==3:
            self.Delete()
        elif ch==4:
            self.DisplayFarmerDatabase()
        else:
            print("Wrong Choice")

    def SignUp(self):
        self.name=input("Enter your name:")
        Farmer.f_id=Farmer.f_id+1
        print("Thanks for registering. Your Farmer Id is ",Farmer.f_id,"\n")
        self.add_Account(self.name,Farmer.f_id)

    def add_Account(self,name,f_id):
        newNode=FarmerNode(name,f_id)
        if Farmer.head is None:
            Farmer.head=newNode
        else:
            n=Farmer.head
            while n.ref is not None:
                n=n.ref
            n.ref=newNode
        global num_of_farmers
        num_of_farmers+=1
            
    def Login(self):
        farmerId=int(input("Enter your Farmer ID:"))
        if self.Authentication(farmerId):
            print("Access Granted")
            n=Farmer.head
            while n is not None:
                if n.FarmerId==farmerId:
                    #n.Processing()
                    n.inputData()
                n=n.ref
        else:
            print("Access Denied!! Wrong Farmer ID\n")

    def Authentication(self,farmerId):
        n=Farmer.head
        while n is not None:
            if n.FarmerId==farmerId:
                return 1
            n=n.ref
        return 0

    def AuthenticationSecurityNum(self,securityNum):
        n=Farmer.head
        while n is not None:
            if n.security_num==securityNum:
                return 1
            n=n.ref
        return 0

    def Delete(self):
        farmerId=int(input("Enter your FarmerId:"))
        global num_of_farmers
        if self.Authentication(farmerId):
            if Farmer.head is None:
                print("List is empty, nothing to delete")
            elif Farmer.head.FarmerId==farmerId:
                Farmer.head=Farmer.head.ref
                num_of_farmers-=1
                print("Delete Successfull!!\n")
            else:
                n=Farmer.head
                while n.ref is not None:
                    if n.ref.FarmerId==farmerId:
                        break
                    n=n.ref
                n.ref=n.ref.ref
                print("Deleted Successfull!!\n")
                num_of_farmers-=1
        else:
            print("Wrong Farmer ID")
        
    def DisplayFarmerDatabase(self):
        n=Farmer.head
        if n==None:
            print("Database Empty!!")
        else:
            while n is not None:
                print("Name=",n.name,"  Money earned=",n.earning)
                n=n.ref
        print()
                
    
class Customer:
    def __init__(self):
        confirmation=input("You are in Customers' portal. Do you want to continue?  y/n:")
        if confirmation=="y":
            self.showItemsAvailable()
        elif confirmation=="n":
            return
        else:
            print("Wrong Choice!!")

    def showItemsAvailable(self):
        global num_of_farmers
        if num_of_farmers==0:
            print(num_of_farmers)
            print("Database is empty. No items available!!\n")
        else:
            n=Farmer.head
            while n is not None:
                self.rand_num=random.randrange(0,100)
                n.security_num=n.FarmerId+self.rand_num
                print("Name=",n.name,"  Farmer ID=",n.security_num)
                n.showData()
                #print()
                n=n.ref
            self.BuyItems();

    def BuyItems(self):
        f_id=int(input("Enter the ID of the farmer from whom you want to buy items or enter -1 if you don't want to buy anything:"))
        if f_id==-1:
            print("Thank You for visiting!!\n")
        else:
            if f.AuthenticationSecurityNum(f_id):
                n=Farmer.head
                while n is not None:
                    if n.security_num==f_id:
                        break
                    n=n.ref
                n.BuyItem()
                
            else:
                print("The entered farmer ID does not exist\n")
    

import random
import os
import sys
f=None
c=None
global num_of_farmers
num_of_farmers=0
def main():
    print("\n--------------WELCOME TO FARMER MANAGEMENT SYSTEM--------------\n\n")
    while 1:
        choice=int(input("Who are you?    1)Farmer  2)Customer  3)Clear screen  -1 to exit:"))
        if choice==-1:
            print("Thanks for visiting!!")
            sys.exit()
        elif choice==1:
            global f
            f=Farmer()
        elif choice==2:
            global c
            c=Customer()
        elif choice==3:
            os.system('cls' if os.name=='nt' else 'clear')
            main()
        else:
            print("Wrong Choice")

main()