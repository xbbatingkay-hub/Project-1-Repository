class Library:
  def borrow_book(self, *args):
    # define the variables
    title = None
    borrower_name = None
    days_to_borrow = None
    # use match-case cuz it looks way cleaner
    match len(args):
      case 1:
        title = args[0]
      case 2:
        title = args[0]
        borrower_name = args[1]
      case 3:
        title = args[0]
        borrower_name = args[1]
        days_to_borrow = args[2]
      case _:
        print("Invalid request.")
        return
    # dreadful nested if-else to print for each case.
    if borrower_name is not None:
      if days_to_borrow is not None:
        print(f"Book \"{title}\" was borrowed by {borrower_name} for {days_to_borrow} days.")
      else:
        print(f"Book \"{title}\" was borrowed by {borrower_name}.")
    else:
      print(f"Book \"{title}\" was borrowed.")

libarby = Library()
libarby.borrow_book("The Adventures of Grimdlebwabble")
libarby.borrow_book("The Adventures of Grimdlebwabble","AntiGoon")
libarby.borrow_book("The Adventures of Grimdlebwabble","AntiGoon",999)
# this one should error
libarby.borrow_book()