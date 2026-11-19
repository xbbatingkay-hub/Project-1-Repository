class Cafeteria:
  def order_food(self, food, quantity=1, drink=None):
    print("Ordered -> ", quantity, food)

    if drink is not None:
      print("plus Drink:",drink)

canteen = Cafeteria()

canteen.order_food("Burger")
canteen.order_food("Burger",2)
canteen.order_food("Burger",1,"CocaCola")