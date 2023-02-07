class hotelparadise:
    

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=250,name='',address='',cindate='',coutdate='',rno=101):

        print(f"{'WELCOME TO FOOD PARADISE' : ^80}")
        import time
        import datetime
        import datetime
        e = datetime.datetime.now()
        print (e.strftime("%d/%m/%Y"))
        print(time.strftime("%H:%M"))

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def staff(self):
        staff = ['RAMAN SHERGIL','DEEPAK KUMAR','RAMESH SINGH','RAJU KUMAR','SHYAM PRASAD','RAMESH SHARMA','DEVENDRA RANA']
        status=[]
        report=[]
        post=['MANAGER','RECEPTONIST','CHEF','WAITER','WAITER','CLEANER','CLEANER']
        print("\n****STAFF MANAGEMENT****")
        N=int(input("\nTOTAL NO. OF STAFF"))
        for x in range(N):
            print('\nNAME:',staff[x])
            print('POST:',post[x])
            d=input(str('PRESENT/ABSENT: '))
            status.append(d)
            e=input(str('REPORTING TIME: '))
            report.append(e)
        import time
        import datetime
        import datetime
        e = datetime.datetime.now()
        print (e.strftime("%d/%m/%Y"))
        print(time.strftime("%H:%M"))
        print("	 *** STAFF RECORD ***\n")
        print("|NAME   | POST | PRESENT/ABSENT | REPORT TIME |")
        print("-----------------------------------------------")
        
        for n in range(N):
            print("| ",staff[n],"|",post[n],"|",status[n],"|",report[n],"|")
    def stock(self):
        print("****STOCK MANAGMENT****")
        n=int(input("Enter the amount of wheat flour present in pantry(in Kgs)"))
      
        if (n<=1000 and n>=500):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of rice present in pantry(in Kgs)"))
      
        if (n<=1000 and n>=500):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of pulses present in pantry(in Kgs)"))
      
        if (n<=500 and n>=200):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of fine flour present in pantry(in Kgs)"))
      
        if (n<=1000 and n>=500):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of oil present in pantry(in Litres)"))
      
        if (n<=300 and n>=100):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of spices present in pantry(in Kgs)"))
      
        if (n<=30 and n>=10):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of sugar present in pantry(in Kgs)"))
      
        if (n<=300 and n>=200):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of salt present in pantry(in Kgs)"))
      
        if (n<=300 and n>=200):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
        n=int(input("\nEnter the amount of tea and coffee present in pantry(in Kgs)"))
      
        if (n<=100 and n>=50):
            print("sufficient amount is present")
        else:
            print("insufficient amount")
    def customer(self):
        print("****CUSTOMER DETAILS****")
        self.name=input("\nEnter your name:")
        self.address=input("Enter your address:")
        self.cindate=input("Enter your check in time:")
        
    


 

        print("*****RESTAURANT MENU*****\n\n")
        print("-------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------")
        print("\n BEVARAGES				 26 Dal Fry................ 140.00")
        print("----------------------------------	 27 Dal Makhani............ 150.00")
        print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
        print(" 2 Masala Tea.............. 25.00")
        print(" 3 Coffee.................. 25.00	 ROTI")
        print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
        print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
        print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
        print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
        print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
        print(" 9 Cheese Toast Sandwich... 70.00")
        print(" 10 Grilled Sandwich........ 70.00	 RICE")
        print("						 ----------------------------------")
        print(" SOUPS				    	 33 Plain Rice.............. 90.00")
        print("----------------------------------	 34 Jeera Rice.............. 90.00")
        print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
        print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
        print(" 13 Veg. Noodle Soup....... 110.00")
        print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
        print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
        print("						 37 Plain Dosa............. 100.00")
        print(" MAIN COURSE				 38 Onion Dosa............. 110.00")
        print("----------------------------------	 39 Masala Dosa............ 130.00")
        print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
        print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
        print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
        print(" 19 Palak Paneer........... 120.00")
        print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
        print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
        print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
        print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
        print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
        print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
        print("\n\nEnter 0 for Billing")


        while (1):

            c=int(input("\n\nEnter your choice:\n"))


            if (c==1 or c==31 or c==32):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+20*d

            elif (c<=4 and c>=2):
                 d=int(input("Enter the quantity:\n"))
                 self.r=self.r+25*d
                 
            elif (c<=6 and c>=5):
                 d=int(input("Enter the quantity:\n"))
                 self.r=self.r+30*d
    
            elif (c<=8 and c>=7):
                 d=int(input("Enter the quantity:\n"))
                 self.r=self.r+50*d
            
            elif (c<=10 and c>=9):
                 d=int(input("Enter the quantity:\n"))
                 self.r=self.r+70*d

            elif (c<=17 and c>=11) or c==35 or c==36 or c==38:
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+110*d

            elif (c<=19 and c>=18):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+120*d

            elif (c<=26 and c>=20) or c==42:
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+140*d

            elif (c<=28 and c>=27):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+150*d

            elif (c<=30 and c>=29):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+15*d

            elif (c==33 or c==34):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+90*d

            elif (c==37):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+100*d

            elif (c<=41 and c>=39):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+130*d

            elif (c<=46 and c>=43):
                d=int(input("Enter the quantity:\n"))
                self.r=self.r+60*d
            elif (c==0):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")
        g=(18/100)*self.r
        print("GST inluded=Rs",g,"\n")
        self.coutdate=input("\nEnter your check out time:")
        print ("\n\n\n******HOTEL BILL******\n")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in time:",self.cindate)
        print ("Check out time:",self.coutdate)
        print ("Your Food bill is:",self.r)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.r+self.a+g,"\n")
        print("Thankyou for visiting!!!!!!\n\n")
        

def main():

    a=hotelparadise()
    

    while (1):
        print("\n1.STAFF MANAGEMENT")
        print("2.STOCK MANAGMENT")
        print("3.MENU CARD")
        print("4.EXIT")
        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.staff()
        elif(b==2):
            a.stock()
        elif (b==3):
            a.customer()
        else:
            quit()



main()
