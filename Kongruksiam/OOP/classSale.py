from classEmployee import Employee

class Sale(Employee):
    __department = "Saler"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__department)
        self.area = area

    # Overriding
    def _showdata(self):
        super()._showdata()
        print(f"Area = {self.area}")

    def __str__(self):
        return (super().__str__() + f"Area = {self.area}")
