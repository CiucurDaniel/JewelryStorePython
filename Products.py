from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import Product


# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    def default(self, o):
        return o.__dict__


class Products:
    """ holds a list with all Product objects """

    products = []

    @classmethod
    def load_products(cls):
        """ reads the products.txt file and re-compose the Python objects
            from the json representation of products. The content of the
            products.txt file should look something like:

            "{\"name\": \"Necklaces\"}"
            "{\"name\": \"Bracelets\"}"

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the products
            list. We have avoided this by overloading the __eq__() operator in
            Products class. More on this during the lectures.
        """
        decoder = Product.Decoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def remove_product(cls, prd):
        """ Removes a product from the products collection. We pass the category
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'categories'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        cls.load_products()
        if prd in cls.products:
            cls.categories.remove(prd)
            with open("categories.txt", 'w') as f:
                for prd in cls.categories:
                    e = Encoder()
                    encoded_prd = e.encode(prd)
                    dump(encoded_prd, f)
                    f.write("\n")

    @classmethod
    def add_product(cls, prd):
        """ Adds a new category in the categories collection. We need to save the
            new category on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        """
        cls.load_products()
        if prd not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_prd = e.encode(prd)
                dump(encoded_prd, f)
                f.write("\n")