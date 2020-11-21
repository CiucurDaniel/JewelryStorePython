from Orders import Orders
from Products import Products
from Product import Bracelet, Earings, Necklace
from Category import Category
from Categories import Categories
from json import JSONDecodeError


from Categories import Categories
from Category import *
import Product


# Function used to display a sub - menu for the Add Product option, in the console

def display_product_menu():
    print("What kind product you want?")
    print("1. Necklace")
    print("2. Earing")
    print("3. Bracelet")

    #TODO: Error handling
    option = int(input())

    if ( option == 1):
        # Necklace
        attributes = input('Please provide: name, price, description, color, material, length separated by comma\n')
        attributes_list = attributes.split(',')
        print(attributes_list)
        newProduct = Necklace(attributes_list[0], attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[5])
        Products.add_product(newProduct)
        print( str(newProduct) + ' added successfully')
        input("\nPress enter key to continue\n")

    elif ( option == 2 ):
        # Earing
        attributes = input('Please provide: name, price, description, color, material, weight separated by comma\n')
        attributes_list = attributes.split(',')
        print(attributes_list)
        newProduct = Earings(attributes_list[0], attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[5])
        Products.add_product(newProduct)
        print( str(newProduct) + ' added successfully')
        input("\nPress enter key to continue\n")

    elif (option == 3):
        # Bracelet
        attributes = input('Please privide: name, price, description, material, length, weight separated by comma\n')
        attributes_list = attributes.split(',')
        print(attributes_list)
        newProduct = Bracelet(attributes_list[0], attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[5])
        Products.add_product(newProduct)
        print( str(newProduct) + ' added successfully')
        input("\nPress enter key to continue\n")

    else:
        pass

#TODO: Create a new function where the above code will be moved
# currently the above function has to many roles which violates a Clean Arhitecture code

# Function used to display the jewlery menu in the console

def displayMainMenu():
    print('|-----------------------------------------|')
    print('| Welcome to Ciucur Daniel Jewlery Shop 1 |')
    print('|-----------------------------------------|')
    print('| 1. Add category                         |')
    print('| 2. Remove category                      |')
    print('| 3. Display categories                   |')
    print('| 4. Add product                          |')
    print('| 5. Remove product                       |')
    print('| 6. Display products                     |')
    print('| 7. Place a new order                    |')
    print('| 8. Display orders                       |')
    print('| 9. Close the program                    |')
    print('|-----------------------------------------|') 

def add_category():
    # read the input and create a new python object
    newCategory = Category(input('What category you want to add?\n'))

    # load the new category in the txt database
    Categories.add_category(newCategory)

    print( str(newCategory) + ' added successfully')
    input("\nPress enter key in order to continue\n")

def remove_category():
    # read the input and create a new python object
    categoryToRemove = Category(input('What category you want to remove?\n'))

    # remove the category
    Categories.remove_category(categoryToRemove)

    print("The category was removed.")
    input("\nPress enter key to continue\n")


def display_categories():
    print('The categories available in the jewlery shop are: \n')

    # Get a list with the categories
    categoriesList = Categories.load_categories()

    # Display the categories retrieved in the list
    for category in categoriesList:
        print(category)

    input("\nPress enter key to continue\n")


def add_product():
    # If the user wants to add a product first see which type he wants to add, display_product_menu()
    display_product_menu()

def remove_product():
    print('In order to remove product you must first display all the products and select the index of the product to delete')
    print("TIP: if you do not know the index of the product you want to delete simply go back and return here aftwards.\n")
    
    # get the index of the product which the use whishes to delete
    productIndex = int(input("Enter the index of the product you wish to delete: "))

    # perform the delete
    try:
            products = Products.load_products()
            # like this because when we list the products we start from 1 because is more friendly to the user
            if 0 < productIndex <= products.__len__():
                productToDelete = products[productIndex - 1]
                Products.remove_product(productToDelete) 
                input("Product: " + str(productToDelete) + " has been removed removed \n Press enter key in order to continue\n")
                
            else:
                product_option = int(input(
                    "This product does not exist in the list. Input 1 to try again or any other number to return to the store menu:\n"))
                if product_option == 1:
                    remove_product()
    except JSONDecodeError:
        input("Error happened while retrieving the products. Press enter key in order to continue\n")


def display_products():
    print('The products available in the jewlery shop are: \n')

    # Index variable is used for deletion purposes
    index = 1
    productsList = Products.load_products()
    print("loaded the list with products")

    for product in productsList:
        print( str(index) + " --> " + str(product) )
        index += 1

    input("\nPress enter key in order to continue\n")

#TODO: Implement
def place_order():
    print('place_order')

def display_orders():
    try:
        orders = Orders.load_orders()
        for index, placed_order in enumerate(orders, start=1):
            print(f"{index}. {placed_order}")
        input("\nPress enter key in order to continue\n")
    except JSONDecodeError:
        input("Error on retrieving the orders\n")

def errorHandler():
    print('This option does not exist\n')


# Simulation a switch using dictionary for user choice in the menu
def menuPicker(option):
    menu = {
        1: add_category,
        2: remove_category,
        3: display_categories,
        4: add_product,
        5: remove_product,
        6: display_products,
        7: place_order,
        8: display_orders
    }

    func = menu.get(option, errorHandler)
    func()


if __name__ == "__main__":
    while(True):
        
        displayMainMenu()
        # Get user's choice
        option = input('Enter your option: ')

        if(option.isnumeric() == False):
            print("Wrong input!")
            break

        num_option = int(option) # convert the user input to int

        # Based on choice go on the function that he requested
        if (num_option != 9):
            menuPicker(num_option)
        else:
            print('Have a nice day, bye!\n')
            break

