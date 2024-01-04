#類別
class friedchicken:
    def __init__(self,name,crispness,spiciness,parts,price):
        self.name = name
        self.crispness = crispness
        self.spiciness = spiciness
        self.parts = parts
        self.price = price

    #更改辣度
    def getspiciness(self):
        return self.spiciness
    def setspiciness(self, new_spiciness):
        self.spiciness = new_spiciness

    #更改部位
    def getparts(self):
        return self.parts
    def setparts(self, new_parts):
        self.parts = new_parts

    #計算服務費5%
    def calculate_servicecharge (self):
        self.price = self.price + (self.price*0.05)
        return self.price

    #打印詳細資料
    def print_details(self):
        print(f"name: {self.name}")
        print(f"crispness: {self.crispness}")
        print(f"spiciness: {self.spiciness}")
        print(f"parts: {self.parts}")
        print(f"price: {self.price}")


#建立物件
chicken1=friedchicken("楓糖香蒜雞","脆皮",2,"大腿肉",180)
chicken2=friedchicken("青花椒香麻雞","脆皮",8,"雞腿",180)
chicken3=friedchicken("上校炸雞","薄皮",0,"雞胸",140)
chicken4=friedchicken("剝皮辣椒雞","薄皮",5,"雞胸",200)


print("Original friedchicken Details:")
chicken1.print_details()
chicken2.print_details()
chicken3.print_details()
chicken4.print_details()


chicken1.setspiciness(4)
chicken1.setparts("雞翅")
chicken1.calculate_servicecharge()
chicken2.setspiciness(10)
chicken2.setparts("雞胸")
chicken2.calculate_servicecharge()
chicken3.setspiciness(1)
chicken3.setparts("大腿肉")
chicken3.calculate_servicecharge()
chicken4.setspiciness(6)
chicken4.setparts("雞腿")
chicken4.calculate_servicecharge()


print ("  ")
print ("  ")
print("Updated friedchicken Details:")
chicken1.print_details()
chicken2.print_details()
chicken3.print_details()
chicken4.print_details()