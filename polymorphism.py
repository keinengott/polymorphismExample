class Product:
    name = ""
    price = 0
    discountPercent = 0.0

    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return round(self.price * self.discountPercent / 100, 2)
    def getDiscountPrice(self):
        return round(self.price - self.getDiscountAmount(), 2)
    def printDescription(self):
        print("This is the product base class")


class Book(Product):
    author = ""

    def __init__(self, name, price, discountPercent, author ):
        Product.__init__(self, name, price, discountPercent)
        self.author = author
    
    def printDescription(self):
        print("This is a book called %s, written by %s. Price is $%s. With a %s %% discount, you save $%s and pay $%s"
              % (self.name, self.author, self.price, self.discountPercent, self.getDiscountAmount(), self.getDiscountPrice()))

class Movie(Product):
    year = 0

    def __init__(self, name, price, discountPercent, year):
        Product.__init__(self, name, price, discountPercent)
        self.year = year

    def printDescription(self):
        print("This is a Movie called %s, filmed in %s. Price is $%s. With a %s %% discount, you save $%s and pay $%s"
              % (self.name, self.year, self.price, self.discountPercent, self.getDiscountAmount(), self.getDiscountPrice()))
        



a = Book("Cosmos", 12.99, 15, "Carl Sagan")
b = Movie("Star Wars", 15.49, 20, 1977)

a.printDescription()
b.printDescription()
