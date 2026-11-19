class Publication:
  def __init__(self, title, author):
    self.__title = title
    self.__author = author

  def get_title(self):
    return self.__title

  def get_author(self):
    return self.__author

  def set_title(self, title):
    self.__title = title

  def set_author(self, author):
    self.__author = author

  def display_info(self):
    print("Publication Info:")
    print(f"Title: {self.__title}\nAuthor: {self.__author}")
    print()

# Made number_of_pages -> num_pages because its too long and the keyboard jams
class Book(Publication):
  def __init__(self, title, author, number_pages):
    self.__title = title
    self.__author = author
    self.__num_pages = number_pages

  def get_number_of_pages(self):
    return self.__num_pages

  def set_number_of_pages(self, number_pages):
    if number_pages < 0:
      return 0
    else:
      self.__num_pages = number_pages
# Made custom display info so that outputting info wont take multiple lines
  def display_info(self):
    print("Book Info:")
    print(f"Title: {self.__title}\nAuthor: {self.__author}\nNumber of Pages: {self.__num_pages}")
    print()

class Magazine(Publication):
  def __init__(self, title, author, issue_number):
    self.__title = title
    self.__author = author
    self.__iss_num = issue_number

  def get_issue_number(self):
    return self.__iss_num

  def set_issue_number(self, issue_number):
    if issue_number < 0:
      return 0
    else:
      self.__iss_num = issue_number
# Made custom display info so that outputting info wont take multiple lines
  def display_info(self):
    print("Magazine Info:")
    print(f"Title: {self.__title}\nAuthor: {self.__author}\nNumber of Pages: {self.__iss_num}")
    print()

pub1 = Publication("GOON GOON GOON 101", "Goon Man")
book1 = Book("Creaming in Cream Land", "Cream Guy", 69696969696969696969696969696969696969)
magazine1 = Magazine("Goons, Tools, and Goon Tools","Various Gooners", 6969)

pub1.display_info()
book1.display_info()
# gets ignored
book1.set_number_of_pages(-100000)
# gets ignored
magazine1.set_issue_number(-100000)
magazine1.display_info()