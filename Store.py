from Order import Order
from Orders import Orders
from Products import Products
from Product import Bracelet, Earings, Necklace
from Category import Category
from Categories import Categories
from json import JSONDecodeError
from Categories import Categories
from Category import *
import Product
from storeStringConstants import MAIN_MENU, PLACE_ORDER_TEXT, PRODUCT_MENU, READ_ENTER_KEY
from datetime import date

# Function used to display a sub - menu for the Add Product option, in the console

def display_product_menu():
    print(PRODUCT_MENU)
    
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

# Function used to display the jewlery menu in the console

def displayMainMenu():
    print(MAIN_MENU)

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
    input(READ_ENTER_KEY)


def display_categories():
    print('The categories available in the jewlery shop are: \n')

    # Get a list with the categories
    categoriesList = Categories.load_categories()

    # Display the categories retrieved in the list
    for category in categoriesList:
        print(category)

    input(READ_ENTER_KEY)


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

    input(READ_ENTER_KEY)

#TODO: Implement
def place_order():
    print('place_order')
    
    userOption = int(input((PLACE_ORDER_TEXT)))

    if ( userOption == 1):
        # User already has a product index
        print("user option 1")
        productIndex = int(input("Enter the index of the product you want to order: "))
        try:
            products = Products.load_products()
            today = date.today().strftime(f"%d/%m/%Y")
            if 0 < productIndex <= products.__len__():
                product_to_order = products[productIndex - 1]
                quantity = 0
                loop = True
                while loop:
                    quantity = int(input("Enter the quantity: \n"))
                    if quantity > 0:
                        loop = False
                shippingAddress = input("Please write the address where this order should be delivered:\n")
                # Order ( product , date, quantity, address)
                clientOrder = Order(product_to_order.__dict__, today, quantity, shippingAddress)
                Orders.add_order(clientOrder)
                input(f"Your order has been placed! " + READ_ENTER_KEY)
        except JSONDecodeError:
            input("Error on retrieving the products. Try again later. " + READ_ENTER_KEY)
    elif ( userOption == 2):
        # User wants to first see the products list
        display_products()
        # After he checked out the products ask why again which one he wants for his order
        place_order()
    elif ( userOption == 3 ):
        # User simply wants to go back
        input(READ_ENTER_KEY)

def display_orders():
    try:
        orders = Orders.load_orders()
        if ( len(orders) >= 1 ):
            print(" The current orders are: ")
        else:
            print("Currently there are no orders.")
        for index, placed_order in enumerate(orders, start=1):
            print(f"{index}. {placed_order}")
        input(READ_ENTER_KEY)
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

