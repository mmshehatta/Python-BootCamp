"""
Certainly! Here are a few more examples of encapsulation in Python:

1.Email Client Class:
    The EmailClient class encapsulates the functionality of sending and receiving emails.
    Private data members store the email server credentials, ensuring that sensitive information is not directly accessible.
    Public methods like send_email() and receive_email() provide controlled access to interact with the email client, ensuring proper encapsulation of data and operations.
    
2.Product Inventory Class:
    The ProductInventory class encapsulates the information and operations related to managing a product inventory.
    Private data members store the inventory items and their quantities, protecting them from direct access.
    Public methods like add_product(), remove_product(), and get_product_quantity() are provided to manage and retrieve product information, promoting encapsulation and data integrity.
    
3.Vehicle Rental System Class:
    The VehicleRentalSystem class encapsulates the functionality of a vehicle rental system.
    Private data members store information about available vehicles, rental rates, and customer records, preventing direct access to these details.
    Public methods like rent_vehicle(), return_vehicle(), and calculate_rental_cost() provide controlled access to interact with the system, maintaining encapsulation and enforcing business rules.
    
4.Library Catalog Class:
    The LibraryCatalog class encapsulates the functionality of a library catalog system.
    Private data members store book details, borrower information, and library policies, hiding them from direct access.
    Public methods like search_book(), borrow_book(), and return_book() are provided to interact with the catalog, ensuring encapsulation and enforcing library rules.
    
5.Geometry Calculator Class:
    The GeometryCalculator class encapsulates the operations related to calculating geometric shapes' properties, such as area and perimeter.
    Private data members store the formulas and constants used for calculations, protecting them from direct access.
    Public methods like calculate_area() and calculate_perimeter() provide controlled access to perform calculations, promoting encapsulation and code reusability.
    
6.Person Class:
    Create a Person class with private attributes such as name and age.
    Provide public methods like get_name() and get_age() to access the private attributes.
    Encapsulating the attributes ensures that they can only be accessed through the defined methods, maintaining data integrity and abstraction.

7.Bank Account Class:
    Create a BankAccount class with private attributes such as account number and balance.
    Provide public methods like deposit() and withdraw() to interact with the account.
    The private attributes are encapsulated, preventing direct access and ensuring that account transactions are performed through the defined methods, enforcing data validation and security.
    
8.Database Connection Class:
    Create a DatabaseConnection class with private attributes such as server address and credentials.
    Provide public methods like connect() and execute_query() to interact with the database.
    Encapsulating the database connection details protects sensitive information and provides a clear interface for working with the database.

These examples demonstrate how encapsulation helps in structuring complex systems, protecting sensitive data, and providing controlled access to functionality. Encapsulation enables modular design, enhances code maintainability, and promotes code reuse by hiding implementation details.
"""

# Certainly! Here's a full example of encapsulation in Python with tests for the Person class:


class Person:
    def __init__(self, name, age):
        self._name = name  # Encapsulated attribute
        self._age = age    # Encapsulated attribute

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


# Tests
person = Person("Alice", 25)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 25


# Here's another example with the BankAccount class and its tests:
class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number  # Encapsulated attribute
        self._balance = 0                     # Encapsulated attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance


# Tests
account = BankAccount("1234567890")
print(account.get_balance())  # Output: 0

account.deposit(100)
print(account.get_balance())  # Output: 100

account.withdraw(50)
print(account.get_balance())  # Output: 50

account.withdraw(100)
# Output: Insufficient funds
print(account.get_balance())  # Output: 50 (balance unchanged)



