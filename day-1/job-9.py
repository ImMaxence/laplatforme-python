class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def displayData(self):
        print(
            "Product name => " + self.name + "\n"
            "Price => " + str(self.price) +"$" + "\n"
            "Quantity => " + str(self.quantity) + "\n"
            )

    def buyProduct(self):
        buyQuantity = int(input("Enter quantity to buy : "))

        if buyQuantity > self.quantity:
            print("Not enough stock")
        else :
            self.quantity = self.quantity - buyQuantity
            print("You buy " + str(buyQuantity) + " items, quantity update !")

    def updatePrice(self, percentage):
        newPriceToAdd = self.price * (percentage / 100)
        self.price = self.price + newPriceToAdd
        print("The price increased by " + str(percentage) + "%")


# Init product and display data
prod = Product("T-shirt", 30, 200)
prod.displayData()

# Buy items and display data
prod.buyProduct()
prod.displayData()

# Item price increase and display data
prod.updatePrice(10)
prod.displayData()

# for run this code => python job-9.py, dont work with code runner extention