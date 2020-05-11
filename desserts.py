"""Dessert classes."""


class Dessert:
    """A dessert."""

    # Dictionary keeping track of dessert stock,
    # with key dessert instance name, value dessert instance
    cache = {}

    # Name of dessert type
    dessert_type = "dessert"

    def __init__(self, name, flavor, price):
        """Initialisation for a Dessert instance."""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<{self.dessert_type.title()} name="{self.name}" qty={self.qty}>'


    def add_stock(self, amount):
        """Update the qty with the amount."""

        self.qty = self.qty + amount


    def sell(self, amount):
        """Sell the given amount of desserts if available and update the qty."""

        if self.qty >= amount:
            # If there are enough desserts, sell them and reduce the qty
            self.qty = self.qty - amount
        elif self.qty == 0:
            # If there are 0 desserts, indicate they're sold out
            print(f"Sorry, these {self.dessert_type}s are sold out")
        else:
            # There are desserts but not enough
            # Sell what's available and update qty to 0
            self.qty = 0


    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale the list of ingredients by the given amount of cupcakes.

        Returns a list of tuples, where each tuple contains the ingredient name
        and scaled amount needed."""

        scaled_ingredients = []

        # Go through each ingredient in the ingredients list and calculate the
        # scaled amount needed, adding it to the scaled_ingredients list
        for ingredient in ingredients:
            ingredient_name, ingredient_qty = ingredient

            scaled_qty = ingredient_qty * amount

            scaled_ingredients.append((ingredient_name, scaled_qty))

        return scaled_ingredients


    @classmethod
    def get(cls, name):
        """Return a cupcake from cls.cache if it exists."""

        dessert = cls.cache.get(name)

        if dessert == None:
            print(f"Sorry, that {cls.dessert_type} doesn't exist")

        return dessert


class Cupcake(Dessert):
    """A cupcake."""

    # Name of dessert type (cupcake)
    dessert_type = "cupcake"

    def __init__(self, name, flavor, price):
        """Initialisation for a Cupcake instance."""

        super().__init__(name, flavor, price)


class Brownie(Dessert):
    """A brownie."""

    # Name of dessert type (brownie)
    dessert_type = "brownie"

    def __init__(self, name, price):
        """Initialisation for a Brownie instance."""

        super().__init__(name, "chocolate", price)


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
