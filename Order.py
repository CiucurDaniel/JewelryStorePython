import copy
from json import JSONEncoder, JSONDecoder, loads


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        values = []
        for key in data.keys():
            values.append(data[key])
        order = Order(*values)
        return order


class Order:
    def __init__(self, product, date, quantity, address):
        self.product = product
        self.date = date
        self.quantity = quantity
        self.address = address

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.product == other.product and self.date == other.date and self.quantity == other.quantity and self.address == other.address

    def __str__(self):
        try:
            return f"Order info: shipping address: {self.address}, quantity: {self.quantity} {'item' if self.quantity == 1 else 'items'}, date: {self.date}, order contains: {self.product}" 
        except AttributeError:
            return "Error on order entry"