class Card:
    def __init__(self,ImageUrl,DeviceType,Price,Rating):
        self.imageUrl=ImageUrl
        self.deviceType=DeviceType
        self.price=Price
        self.rating=Rating
    def details(self):
        print("imageUrl:",self.imageUrl)
        print("deviceType:",self.deviceType)
        print("price:",self.price)
        print("rating:",self.rating)
        
Product1=Card("Dummy-url 1","Mobile",56000,4.5)
print("Product - 1 :")
Product1.details()
print()

Product2=Card("Dummy-url 2","Laptop",94000,4.8)
print("Product - 2 :")
Product2.details()
print()

Product3=Card("Dummy-url 3","Smart-watch",18000,3.5)
print("Product - 3 :")
Product3.details()
print()
