class Cafeteria:
  def order_food(self, *args):
    if len(args) == 1:
      food = args[0]
      quantity = 1
      drink = None

    elif len(args) == 2:
      food = args[0]
      quantity = args[1]
      drink = None

    elif len(args) == 3: # maybe use match-case for these conditions instead? itll look cleaner
      food = args[0]
      quantity = args[1]
      drink = args[2]

    else:
      print("Invalid order!")
      return

    print("Ordered ->", quantity, food)

    if drink is not None:
      print("Plus Drink:", drink)

canteen = Cafeteria()
canteen.order_food("Burger")
canteen.order_food("Burger",2)
canteen.order_food("Burger",1,"CocaCola")