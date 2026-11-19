# Complete the TODO sections in the starter code below:
# ============================================================
# TASK 1: ENCAPSULATION (10 Points)
# ============================================================
class MenuItem:
    # TODO 1:MenuItem Constructor
        #  Define private attribute item_id using item_id
        #  Define public attributes name and base_price using name and base_price
        #  Define private attribute rating set default to 5.0
    def __init__(self, item_id: str, float, name: str, base_price: float, rating=5.0):
        self.__item_id = item_id
        self.__rating = rating
        self.name = name
        self.base_price = base_price

    #Getter for private attributes:  item_id and  rating
    # TODO 2: Return private item_id and rating
    def get_item_id(self):
        return self.__item_id

    def get_rating(self):
        return self.__rating

    def set_rating(self, new_rating: float):
        # TODO 3: Update attribute rating ONLY if new_rating is between 1.0 and 5.0
        # Otherwise, print: "Invalid rating! Must be between 1.0 and 5.0."
        if new_rating >= 1.0 and new_rating <= 5.0:
            self.__rating = new_rating
        else:
            print("Invalid rating! Must be between 1.0 and 5.0.")

    def calculate_price(self):
        return self.base_price

    def get_details(self):
        return f"{self.name} - P{self.calculate_price():.2f} (Rating: {self.__rating}/5.0)"


# ============================================================
# TASK 2: INHERITANCE, OVERRIDING & OVERLOADING (20 Points)
# ============================================================
# class PizzaItem fill in the blank
# PizzaItem is a child class of MenuItem
class PizzaItem(MenuItem):
    def __init__(self, item_id: str, name: str, base_price: float, size: str, rating=5.0):
        # TODO 4: Define the constructor of PizzeItem class
        # Define public attribute size. Actual values are "Small", "Medium", or "Large"
        super().__init__(item_id, base_price, name, rating)
        self.size = size
        self.toppings = []   #list of toppings

    # Method Overloading via Default Parameter
    def add_topping(self, topping_name: str, extra_cost: float = 10.00):
        self.toppings.append(topping_name)
        self.base_price += extra_cost

    # Method Overriding
    def calculate_price(self):
      # TODO 6: Return total price based on size:
      # - "Medium" adds Php25.00 to base_price
      # - "Large" adds Php50.00 to base_price
      # - "Small" adds Php0.00
      size_price = 0.00
      match self.size:
          case "Small":
              size_price = 0.00
          case "Medium":
              size_price = 25.00
          case "Large":
              size_price = 50.00
      return self.base_price + size_price

    # Method Overriding
    def get_details(self):
        # TODO 7: Return formatted details:
        # Print the pizza size, name, number of toppings, price and rating.
        # e.g., "(Large) Pepperoni Pizza (with 2 topping(s)) - 280.00 (Rating: 4.8/5.0)"
        return f"({self.size}) {self.name} (with {len(self.toppings)} topping(s) - P{self.calculate_price():.2f} (Rating: {self.get_rating()}/5.0)"


# DrinkItem is a child class of MenuItem
# class DrinkItem fill in the blank
class DrinkItem(MenuItem):
    def __init__(self, item_id: str, name: str, base_price: float, is_cold: bool, rating = 5.0):
        super().__init__(item_id, base_price, name, rating)
        self.is_cold = is_cold

    # Method Overriding
    def calculate_price(self):
        # TODO 9: If is_cold is True, add Php1.00 to base_price. Otherwise return base_price.
        if self.is_cold:
          self.base_price += 1.00
        return self.base_price

    # Method Overriding
    def get_details(self):
        # TODO 10: Return formatted details including "(Cold)" or "(Hot)"
        # e.g., "Cold C2 Green Tea - Php16.00 (Rating: 5.0/5.0)"
        temp = "Hot"
        if self.is_cold:
            temp = "Cold"
        return f"{temp} {self.name} - P{self.calculate_price():.2f} (Rating: {self.get_rating()}/5.0)"


# ============================================================
# TASK 3: POLYMORPHISM (10 Points)
# ============================================================
class FoodOrder:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        # Polymorphic call: item.calculate_price() resolves dynamically for each class
        # TODO 11: Loop through self.items and sum the result of item.calculate_price()
        total_price = 0
        for items in self.items:
          total_price += items.calculate_price()
        return total_price


    #Fill in the blank - print the customer name
    def print_receipt(self):
        print(f"\n>>MegaBites Receipt for {self.customer_name}")
        print("-" * 50)
        # TODO 12: Loop through self.items and print item.get_details() for each item
        for item in self.items:
            print(item.get_details())
        print("-" * 50)
        print(f"Total Amount Due: P{self.calculate_total():.2f}")


# ============================================================
# TEST & VERIFICATION (10 Points)
# ============================================================
if __name__ == "__main__":
    print(">>1. Testing Encapsulation")
    pizza = PizzaItem("P01", "Pepperoni Pizza", 200.00, "Large")
    print(pizza.base_price)
    pizza.set_rating(4.0)    # Valid update
    pizza.set_rating(6.5)    # Invalid: Should display error message!

    print("\n>>2. Testing Method Overloading")
    #TODO 13: Add pizza topping: Extra Cheese (used default argument) and Smoked Bacon at P20.00
    pizza.add_topping("Extra Cheese")      # Uses default
    pizza.add_topping("Smoked Bacon", 20.00)

    print("\n>>3. Testing Inheritance & Polymorphism")
    #TODO 14: Instantiate DrinkItem : A cold C2 Green Tea at 15.00 with item_id D01
    drink = DrinkItem("D01", "C2 Green Tea", 15.00, True)

    #TODO 15: Fill in the blanks - add pizza and drink MenuItems to order
    order = FoodOrder("Leslie")
    order.add_item(pizza)
    order.add_item(drink)

    order.print_receipt()