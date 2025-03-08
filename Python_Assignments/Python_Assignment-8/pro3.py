# 3.
# Create a class product having (pid and manufacture_location) as Protected fields,Create another class as Book having (name, number_of_pages,author,price) as private fields. Specify _init(), getters, setters, __str_() , print_data() Use correct OOP feature to implement this scenario.
# a) display the details of the product and book
# b) check if book price is 0 or negative then price is not valid otherwise print valid price.


class Product:
    def __init__(self,pid,manufacture_location):
        self._pid=pid
        self._manufacture_location=manufacture_location

class Book(Product):
    def __init__(self,pid,manufacture_location,name,number_of_pages,author,price):
        Product.__init__(self,pid,manufacture_location)
        self.__name=name
        self.__number_of_pages=number_of_pages
        self.__author=author
        self.__price=price

    def display(self):
        print(f"Book Id: {self._pid}")
        print(f"Book manufacture_location: {self._manufacture_location}")
        print(f"Book name: {self.__name}")
        print(f"Book author: {self.__author}")

        if self.__price <= 0:
            print("Price is not valid.")
        else:
            print("Valid price.")
        print(f"Book price: {self.__price}")
        

b=Book(10,"pune","Python",100,"anu",999)
b.display()