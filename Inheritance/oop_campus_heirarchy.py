#==============================
# Basic Student Conduct Officer
#==============================
class SCOfficer:
  def __init__(self, name, id_num):
    self.__name = name
    self.__id_num = id_num

  def display_info(self):
    print(f"SCO Officer Basic ID Details:\nName: {self.__name}\nID #: {self.__id_num}")

  def officing(self, student):
    print(f"Making a case against {student.name}...")
    if student.did_crime == True:
      print(f"NCR NCR NCRRRRRRRR")
    else:
      print(f"Ok you good :aggresive thumbs up:")

#=================================
# Student Conduct Officer Chairman
#=================================
class SCO_Chairman(SCOfficer):
  def __init__(self, name, id_num):
    super().__init__(name, id_num)

  def display_info(self):
    super().display_info()

  def officing(self, student):
    super().officing(student)

  def do_chair_things(self):
    print("Doing chair things!\n1. Sit on chair\n2. Attend meeting\n3. New offences (NCRNCRNCRRR)\n4. Drink coffee")

#==============================
# G7-G9 Student Conduct Officer
#==============================
class G7_9_SCOfficer(SCOfficer):
  def __init__(self, name, id_num):
    super().__init__(name, id_num)

  def display_info(self):
    super().display_info()

  def officing(self, student):
    if student.grade >= 7 and student.grade <= 9:
      super().officing(student)
    else:
      print("not my department dude")

# Student that is a chud
class Stchudent:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
    self.did_crime = False

  def do_crime(self):
    self.did_crime = True

#================
# Test stuff out!
#================

# create specialized student conduct officer
scoff_1 = G7_9_SCOfficer("Officer Guy","777-77")
scoff_1.display_info()
# create a student guy thats a bum
student_guy = Stchudent("bum",7)

# what a bad student!
student_guy.do_crime()

# hmm... Officer guy didnt like that...
scoff_1.officing(student_guy)

# Output: NCR NCR NCRRRRRRRR

# The chairman appears!
schairman = SCO_Chairman("Goated Officer","999-99")
schairman.display_info()

# do stuff!
schairman.do_chair_things()

# create a student guy thats a bum...but older???
student_guy2 = Stchudent("greater bum",12)
# greater bum sells "substances" to kids!
student_guy2.do_crime()

# Goated Officer didnt like that...
schairman.officing(student_guy2)