# 1. Create a class named Mobile with attributes ModelName,Company,Price and with
#   methods:set_attributes, print_details and can_afford


class Mobile:
    
    def __init__(self, modelname,company,price):
        setattr(self, "ModelName", modelname)
        setattr(self, "Company", company)
        setattr(self, "price", price)

    def ModelName():
        pass
    def Comapny():
        pass
    def Price(self):
        print(f" {getattr(self, 'ModelName')}")
        print(f" {getattr(self, 'Company')}")
        print(f" {getattr(self, 'price')}")



mo=Mobile("S21","Samsung",20000)
mo.Price()


# setattr(object, attribute_name, value)