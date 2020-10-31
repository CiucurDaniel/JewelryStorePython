# File which has defined the products of the store
# making use of OOP concepts such as inheritance
#
# author: Daniel Ciucur
# date : 13 Oct 2020
#

from Category import Category
from json import JSONEncoder, JSONDecoder, loads
from abc import ABC, ABCMeta, abstractmethod
from typing import overload

# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])

        #prd = Category(*vals)
        # Here we first need to check what kind of object we have
        prd = None

        if( vals[0] == 'Necklace'):
            prd = Necklace(*vals)
        elif (vals[0] == 'Bracelet'):
            prd = Bracelet(*vals)
        elif ( vals[0] == 'Earings'):
            prd = Earings(*vals)
        return prd


# Product abstract class which will be 
# the base class for the other concrete types
# of products we will have in the store

class Product(metaclass=ABCMeta):
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        # TODO: Add category attiribute and isOrdered Boolean Attribute
        #self.category = category
        #self.isOrdered = False # a new added products is surely not ordered yet


class Necklace(Product):
    def __init__(self, name, price, description, color, material, length ):
        super(Necklace, self).__init__(name, price, description)
        self.color = color
        self.material = material
        self.length = length
    
    
class Bracelet(Product):
    def __init__(self, name, price, description, color, material, weight):
        super(Bracelet, self).__init__(name, price, description)
        self.color = color
        self.material = material
        self.weight = weight

class Earings(Product):
    def __init__(self, name, price, description, material, length, weight):
        super(Earings, self).__init__(name, price, description)
        self.material = material
        self.length = length
        self.weight = weight


#Use the Person class to create an object, and then execute the printname method:

x = Product("Necklace", 125, "lantisor de argint 12mm circ")
#x.printProduct()

y = Earings('cercei', 1234, 'bla bla bla', 'aur', 12, 100)
#y.printProduct()

#####3
