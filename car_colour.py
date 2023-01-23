class COMPANY:
    price=[]

    def add_items(self,cost):
        self.price.append(cost)

class MAHINDRA(COMPANY):
    def type_car(self,type,colour):
        self.type=type
        self.colour=colour
        print(f"car company : MAHINDRA , type of car : {self.type}")
        if self.type=="electric":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if self.colour=="black":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*29/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*28.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*28/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*27.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*27/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*26.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*26/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*25.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*25/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*24.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*24/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*23.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        elif self.type=="diesel":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if self.colour=="black":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*11/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*11.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*12/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*12.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*13/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*13.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*14/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*14.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*15/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*15.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*16/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*16.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        elif self.type=="petrol":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if self.colour=="black":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*23/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*22.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*22/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*21.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*21/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*20.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*20/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*19.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="XUV100":
                        for y in self.price:
                            z=y+(y*19/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV210":
                        for y in self.price:
                            z=y+(y*18.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV300":
                        for y in self.price:
                            z=y+(y*18/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="XUV400":
                        for y in self.price:
                            z=y+(y*17.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        else :
            print ("valid type of the car ")
    
class TATA(COMPANY): 
    def type_car(self,type,colour): 
        self.type=type
        self.colour=colour
        print(f"car company : TATA , type of car : {self.type}")
        if self.type=="electric":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if self.colour=="black":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*24/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*23.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*23/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*22.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*22/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*21.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*21/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*20.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*20/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*19.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*19/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*18.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        elif self.type=="diesel":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if self.colour=="black":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*12/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*11.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*11/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*10.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*10/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*9.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*9/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*8.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*8/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*7.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*7/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*6.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        elif self.type=="petrol":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if self.colour=="black":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*18/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*17.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*17/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*16.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="white":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*16/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*15.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*15/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*14.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
                elif self.colour=="red":
                    if i=="DFD":
                        for y in self.price:
                            z=y+(y*14/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="FDFR":
                        for y in self.price:
                            z=y+(y*13.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSRF":
                        for y in self.price:
                            z=y+(y*13/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    elif i=="DSEF":
                        for y in self.price:
                            z=y+(y*12.5/100)
                            print(f"model of the car : {i} , colour of the car : {self.colour} , cost of the car : {z}")
                    else:
                        print(f"enter valid details : {i}")
        else :
            print ("valid type of the car ")


                



                    


com=COMPANY()
com.add_items(1200000)

model=MAHINDRA()
model.type_car("electric","black")
model.type_car("electric","red")
model.type_car("electric","white")
model.type_car("diesel","black")
model.type_car("diesel","red")
model.type_car("diesel","white")
model.type_car("petrol","red")
model.type_car("petrol","black")
model.type_car("petrol","white")

model=TATA()
model.type_car("electric","red")
model.type_car("electric","black")
model.type_car("electric","white")
model.type_car("diesel","white")
model.type_car("diesel","red")
model.type_car("diesel","black")
model.type_car("petrol","black")
model.type_car("petrol","white")
model.type_car("petrol","red")
