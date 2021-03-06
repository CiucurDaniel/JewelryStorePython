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

        # Here we first need to check what kind of object we have
        prd = None

        if( vals[-1] == 'Necklace'):
            #print('Decoded a necklace')
            vals.pop() # pop out the object type, we do not need it as it is assigned by default in the constr
            prd = Necklace(*vals)

        elif (vals[-1] == 'Bracelet'):
            #print('Decoded a bracelet')
            vals.pop() # pop out the object type, we do not need it as it is assigned by default in the constr
            prd = Bracelet(*vals)

        elif ( vals[-1] == 'Earings'):
            #print('Decoded some earings')
            vals.pop() # pop out the object type, we do not need it as it is assigned by default in the constr
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

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.description == self.description


class Necklace(Product):
    def __init__(self, name, price, description, color, material, length ):
        super(Necklace, self).__init__(name, price, description)
        self.color = color
        self.material = material
        self.length = length
        self.type = 'Necklace' # this will help with object deconding from JSON

    def __eq__(self, other):
        return super().__eq__(other) and self.__class__ == other.__class__ and self.color == other.color and self.material == other.material and self.length == other.length

    def __str__(self):
        return f"Necklace: {self.name}, price: {self.price} RON, description: {self.description}, material {self.material}, color {self.color}, length {self.length} cm"
    

class Bracelet(Product):
    def __init__(self, name, price, description, color, material, weight):
        super(Bracelet, self).__init__(name, price, description)
        self.color = color
        self.material = material
        self.weight = weight
        self.type = 'Bracelet' # this will help with object deconding from JSON

    def __eq__(self, other):
        return super().__eq__(other) and self.__class__ == other.__class__ and self.color == other.color and self.material == other.material and self.weight == other.weight

    def __str__(self):
        return f"Necklace: {self.name}, price: {self.price} RON, description: {self.description}, material {self.material}, color {self.color}, weight {self.weight} grams"


class Earings(Product):
    def __init__(self, name, price, description, material, length, weight):
        super(Earings, self).__init__(name, price, description)
        self.material = material
        self.length = length
        self.weight = weight
        self.type = 'Earings' # this will help with object deconding from JSON

    def __eq__(self, other):
        return super().__eq__(other) and self.__class__ == other.__class__ and self.material == other.material and self.length == other.length and self.weight == other.weight

    def __str__(self):
        return f"Necklace: {self.name}, price: {self.price} RON, description: {self.description}, material {self.material}, length {self.length}, weight {self.weight} grams"
