from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
import Category


# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    def default(self, o):
        return o.__dict__


class Categories:
    """ holds a list with all Category objects """

    categories = []

    @classmethod
    def load_categories(cls):
        """ reads the categories.txt file and re-compose the Python objects
            from the json representation of categories. The content of the
            categories.txt file should look something like:

            "{\"name\": \"Necklaces\"}"
            "{\"name\": \"Bracelets\"}"

            Basically, we read the file line by line and from those lines we
            recreate the Pyhton objects.

            Also we take care to not multiply the elements in the categories
            list. We have avoided this by overloading the __eq__() operator in
            Category class. More on this during the lectures.
        """
        decoder = Category.Decoder()

        try:
            with open("categories.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_category = decoder.decode(data)
                    if decoded_category not in cls.categories:
                        cls.categories.append(decoded_category)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
        return cls.categories

    @classmethod
    def remove_category(cls, cat):
        """ Removes a category from the categories collection. We pass the category
            to be removed as a parameter to teh function and then, as a first step
            we remove it from the class variable 'categories'. Then, in a second step
            we iterate that collection and we serialize element by element
        """
        cls.load_categories()
        if cat in cls.categories:
            cls.categories.remove(cat)
            with open("categories.txt", 'w') as f:
                for cat in cls.categories:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")

    @classmethod
    def add_category(cls, cat):
        """ Adds a new category in the categories collection. We need to save the
            new category on the disk too, so we have to call teh Encoder class to
            transform teh Python object in a JSON representation
        """
        cls.load_categories()
        if cat not in cls.categories:
            with open("categories.txt", 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")