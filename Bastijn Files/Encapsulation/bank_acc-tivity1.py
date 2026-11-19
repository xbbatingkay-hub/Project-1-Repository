# traditional
class BankAcc:
  def __init__(self, name, money):
    self.__name = name
    self.__money = money

  # Getter
  def get_money(self):
    return self.__money

  # Setter
  def set_money(self, new_money):
    if new_money > 0:
      if new_money >= 500000:
        print("This is a suspicious transaction. Try to lower the amount you will set.")
      else:
        self.__money = new_money
        print("Money set successfully.")
    else:
      print("New money value should be greater than zero.")

cool_bank = BankAcc("Goon Man", 10)
#added print()
print(cool_bank.get_money())
cool_bank.set_money(100)

print()
print(cool_bank.get_money())

print()
cool_bank.set_money(10000000000000000000)
print(cool_bank.get_money())