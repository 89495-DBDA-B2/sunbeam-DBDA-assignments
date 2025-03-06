# 3.
# Create a class product having (pid and manufacture_location) as private fields,Create another class as Book having (name, number_of_pages,author,price) as private fields. Specify _init(), getters, setters, __str_() , print_data() Use correct OOP feature to implement this scenario.
# a) display the details of the product and book
# b) check if book price is 0 or negative then price is not valid otherwise print valid price.




class Product:
    def __init__(self, pid, manufacture_location):
        # Private fields
        self.__pid = pid
        self.__manufacture_location = manufacture_location

    # Getter methods
    def get_pid(self):
        return self.__pid

    def get_manufacture_location(self):
        return self.__manufacture_location

    # Setter methods
    def set_pid(self, pid):
        self.__pid = pid

    def set_manufacture_location(self, location):
        self.__manufacture_location = location

    # __str__ method to represent Product as a string
    def __str__(self):
        return f"Product ID: {self.__pid}, Manufacture Location: {self.__manufacture_location}"


class Book(Product):
    def __init__(self, pid, manufacture_location, name, number_of_pages, author, price):
        # Initialize parent class (Product) attributes using super()
        super().__init__(pid, manufacture_location)
        # Private fields specific to Book class
        self.__name = name
        self.__number_of_pages = number_of_pages
        self.__author = author
        self.__price = price

    # Getter methods
    def get_name(self):
        return self.__name

    def get_number_of_pages(self):
        return self.__number_of_pages

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_number_of_pages(self, number_of_pages):
        self.__number_of_pages = number_of_pages

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    # Validate price method
    def check_valid_price(self):
        if self.__price <= 0:
            print("Price is not valid.")
        else:
            print("Valid price.")

    # Method to display the details of Product and Book
    def print_data(self):
        # Print Product details
        print(super().__str__())  # Call Product's __str__ method
        # Print Book details
        print(f"Book Name: {self.__name}")
        print(f"Number of Pages: {self.__number_of_pages}")
        print(f"Author: {self.__author}")
        print(f"Price: {self.__price}")
        self.check_valid_price()  # Check if the price is valid

    # __str__ method to represent Book as a string
    def __str__(self):
        return f"Book Name: {self.__name}, Author: {self.__author}, Pages: {self.__number_of_pages}, Price: {self.__price}"


# Example usage:

# Create a Book object
book = Book(1, "USA", "Python Programming", 500, "John Doe", 300)

# Print Book and Product details
book.print_data()

# Print the string representation of the book
print("\nString Representation of Book:")
print(book)

# Try setting an invalid price and checking
book.set_price(-50)
book.print_data()
