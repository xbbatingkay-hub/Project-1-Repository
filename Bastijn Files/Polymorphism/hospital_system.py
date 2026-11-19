class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount
    def display_info(self):
        print(f"Patient Name: {self.__name}\nOriginal Bill: ₱{self.__bill_amount}\nFinal Bill: ₱{self.calculate_bill()}")

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        self.__name = name
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount - self.__bill_amount * 0.20

class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        # Name mangling requires you to make the attributes for the child too fuh
        # Maybe this can be bypassed using protected variables with only one "_"
        self.__name = name
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount - self.__bill_amount * 0.15

patient1 = Patient("Goon Man Junior", 6767676767676767.00)
patient2 = SeniorPatient("Goon Male", 6969696969696969.00)
patient3 = PhilHealth_Patient("Cream Guy", 696969696969696969696969696969.00)

print("Hosjpitalio Enfo")
print("----------------------------------")
patient1.display_info()
print("----------------------------------")
patient2.display_info()
print("----------------------------------")
patient3.display_info()
print("----------------------------------")