class car:
    def __init__(self, name, model, wheels):
        self.name = name
        self.model = model
        self.wheels = wheels

    def display(self):
        print("Brand is ", self.name)
        print("model is ", self.model)
        print("no of wheels ", self.wheels)


class purchase(car):
    def __init__(self, name, model, wheels, price, payment_type):
        super().__init__(name, model, wheels)
        self.price = price
        self.payment_type = payment_type

    def display(self):
        super().display()
        print("price", self.price)
        print("payment_type", self.payment_type)

ob = purchase("bmw", "x1", 4, "37L", "cheque")
ob.display()