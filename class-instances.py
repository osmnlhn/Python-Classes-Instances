class Myclass:
    a=5
    def hello(self):
        print("Hello,World")
my=Myclass()
print(my.a)
print(my.hello())
###########################################
class House:
    
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        
    
house = House()
print(house.num_rooms)
print(House.num_rooms)

##############################################

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)

##############################################

class Recipe():
    def __init__(self,dish,items,time) -> None:
        self.dish=dish
        self.items=items
        self.time=time
    
    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + " and takes " + str(self.time)+ " min to prepare ")

pizza=Recipe("Pizza",["cheese","bread","tomato"],45)
pasta=Recipe("Pasta",["bread","tomato"],50)


print(pizza.contents())
print(pasta.contents())

###################################################################################
class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name=name
        self.payment=payment
        self.amount=amount
    
    def pay(self):
        self.payment="yes"

    def status(self):
        if self.payment=="yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan=Payslips("Nathan","no",1000)
roger=Payslips("roger","no",3000)

print(nathan.status()," \n ",roger.status())

nathan.pay()
print("After Payment")
print(nathan.status(),"\n",roger.status())

roger.pay()
print("After Payment")
print(nathan.status(),"\n",roger.status())



        