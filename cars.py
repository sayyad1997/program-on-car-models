class COMPANY:
    price=[]

    def add_items(self,cost):
        self.price.append(cost)

class MAHINDRA(COMPANY):
    def type_car(self,type):
        self.type=type
        print(f"car company : MAHINDRA , type of car : {self.type}")
        if self.type=="electric":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if i=="XUV100":
                    for y in self.price:
                        z=y+(y*18/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV210":
                    for y in self.price:
                        z=y+(y*16/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV300":
                    for y in self.price:
                        z=y+(y*17/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV400":
                    for y in self.price:
                        z=y+(y*19/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")
        elif self.type=="diesel":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if i=="XUV100":
                    for y in self.price:
                        z=y+(y*12/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV210":
                    for y in self.price:
                        z=y+(y*13/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV300":
                    for y in self.price:
                        z=y+(y*14/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV400":
                    for y in self.price:
                        z=y+(y*15/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")
        elif self.type=="petrol":
            x=["XUV100","XUV210","XUV300","XUV400"]
            for i in x:
                if i=="XUV100":
                    for y in self.price:
                        z=y+(y*12.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV210":
                    for y in self.price:
                        z=y+(y*13.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV300":
                    for y in self.price:
                        z=y+(y*14.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="XUV400":
                    for y in self.price:
                        z=y+(y*15.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")

        else :
            print ("valid type of the car ")
    
class TATA(COMPANY): 
    def type_car(self,type): 
        self.type=type
        print(f"car company : TATA , type of car : {self.type}")
        if self.type=="electric":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if i=="DFD":
                    for y in self.price:
                        z=y+(y*17/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="FDFR":
                    for y in self.price:
                        z=y+(y*16.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSRF":
                    for y in self.price:
                        z=y+(y*18/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSEF":
                    for y in self.price:
                        z=y+(y*18.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")
        elif self.type=="diesel":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if i=="DFD":
                    for y in self.price:
                        z=y+(y*10/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="FDFR":
                    for y in self.price:
                        z=y+(y*12/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSRF":
                    for y in self.price:
                        z=y+(y*13/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSEF":
                    for y in self.price:
                        z=y+(y*14/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")
        elif self.type=="petrol":
            x=["DFD","FDFR","DSRF","DSEF"]
            for i in x:
                if i=="DFD":
                    for y in self.price:
                        z=y+(y*10.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="FDFR":
                    for y in self.price:
                        z=y+(y*12.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSRF":
                    for y in self.price:
                        z=y+(y*13.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                elif i=="DSEF":
                    for y in self.price:
                        z=y+(y*14.5/100)
                        print(f"model of the car : {i} , cost of the car : {z}")
                else:
                    print(f"enter valid details : {i}")

        else :
            print ("valid type of the car ")


                



                    


com=COMPANY()
com.add_items(1200000)

model=MAHINDRA()
model.type_car("electric")
model.type_car("diesel")
model.type_car("petrol")

model=TATA()
model.type_car("electric")
model.type_car("diesel")
model.type_car("petrol")