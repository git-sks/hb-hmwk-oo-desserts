"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    # Dictionary w/ key cupcake instance name, value cupcake instance
    cache = {}

    def __init__(self, name, flavor, price):
        """Initialisation for a Cupcake instance."""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def add_stock(self, amount):
        """Update the qty with the amount."""

        self.qty = self.qty + amount


    def sell(self, amount):
        """Sell the given amount of cupcakes if available and update the qty."""

        if self.qty >= amount:
            # If there are enough cupcakes, sell them and reduce the qty
            self.qty = self.qty - amount
        elif self.qty == 0:
            # If there are 0 cupcakes, indicate they're sold out
            print("Sorry, these cupcakes are sold out")
        else:
            # There are cupcakes but not enough
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

        cupcake = cls.cache.get(name)

        if cupcake == None:
            print("Sorry, that cupcake doesn't exist")

        return cupcake


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
