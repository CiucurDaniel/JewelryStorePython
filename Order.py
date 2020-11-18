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
    def __init__(self, product, product_type, quantity, address):
        self.product = product
        self.product_type = product_type
        self.quantity = quantity
        self.address = address

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.product == other.product and self.product_type == other.product_type and self.quantity == other.quantity and self.address == other.address

    # a deepcopy is created so the self.product dictionary won't be affected when changing the content
    # although creating a Product object to use its print method would have been a better solution, for the sake of the project printing the dict content should suffice
    def __str__(self):
        try:
            product_dict = copy.deepcopy(self.product)
            category_name = product_dict.get('category').get('name')
            product_dict.pop('category')
            return f"Order to {self.address}, containing {self.quantity} {'item' if self.quantity == 1 else 'items'} of {self.product_type}: {product_dict} from category {category_name}"
        except AttributeError:
            return "Error on order entry"