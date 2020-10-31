from Products import Products
from Product import Earings, Necklace
from Category import Category
from Categories import Categories
from json import JSONDecodeError

# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier

from Categories import Categories
from Category import *
import Product

def display_product_menu():
    print("What kind product you want?")
    print("1. Necklace")
    print("2. Earing")
    print("3. Bracelet")

    option = int(input())

    if ( option == 1):
        # Necklace
        attributes = input('Please provide: name, price, description, color, material, length')
        attributes_list = attributes.split()
        print(attributes_list)
        newProduct = Necklace(attributes_list[0], attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[5])
        Products.add_product(newProduct)
        print( str(newProduct) + ' added successfully')

    elif ( option == 2 ):
        # Earing
        attributes = input('Please provide: name, price, description, color, material, weight')
        attributes_list = attributes.split()
        print(attributes_list)
        Earings()

    elif (option == 3):
        # Bracelet
        attributes = input('Please privide: name, price, description, material, length, weight')
        attributes_list = attributes.split()
        print(attributes_list)

    else:
        pass


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
    newCategory = Category(input('What category you want to add?'))

    # load the new category in the txt database
    Categories.add_category(newCategory)

    print( str(newCategory) + ' added successfully')

def remove_category():
    # read the input and create a new python object
    categoryToRemove = Category(input('What category you want to remove?'))

    # load the new category in the txt database
    Categories.remove_category(categoryToRemove)

    print("The category was removed.")


def display_categories():
    print('The categories available in the jewlery shop are: ')

    categoriesList = []
    Categories.load_categories()

    for category in Categories.categories:
        print(category)


def add_product():
    display_product_menu()

def remove_product():
    print('remove_product')

def display_products():
    print('display_produts')

def place_order():
    print('place_order')

def display_orders():
    print('display_orders')

def errorHandler():
    print('This option does not exist')


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
        option = int(input('Enter your option:'))
        # TODO: Provide error handling for non int characters

        # Based on choice go on the function that he requested
        if (option != 9):
            menuPicker(option)
        else:
            print('Have a nice day, bye!')
            break