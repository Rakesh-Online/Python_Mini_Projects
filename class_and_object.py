class mobile:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("object is created")

    def dispaly(self):
        print("Mobile name is: ", self.name)
        print("Price of the mobile is :", self.price)

m1 = mobile("Iphone", 80000)

m1.dispaly()