class Merchandise:
    def __init__(self, name, price, image_url):
        self.name = name
        self.price = price
        self.image_url = image_url


merchandise1 = Merchandise("Arts in India T-Shirt", 20,
                           "https://www.example.com/arts-in-india-tshirt.jpg")

assert merchandise1.name == "Arts in India T-Shirt"
assert merchandise1.price == 20
assert merchandise1.image_url == "https://www.example.com/arts-in-india-tshirt.jpg"
print("test1 passed")
merchandise2 = Merchandise("Emerging Talent Tote Bag", 10,
                           "https://www.example.com/emerging-talent-totebag.jpg")

assert merchandise2.name == "Emerging Talent Tote Bag"
assert merchandise2.price == 10
assert merchandise2.image_url == "https://www.example.com/emerging-talent-totebag.jpg"
print("test2 passed")
merchandise3 = Merchandise(
    "Art Print Set", 30, "https://www.example.com/art-print-set.jpg")

# assertion error expected name is Art Print Set
assert merchandise3.name == "Classical Art", "Expected name is Art Print Set"
assert merchandise3.price == 30
assert merchandise3.image_url == "https://www.example.com/art-print-set.jpg"
print("test3 passed")
