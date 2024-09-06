from classEmployee import Employee

class Programmer(Employee):
    __department = "Developer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__department)
        self.exp = experience
        self.skill = skill

    # Overrinding
    def _showdata(self):
        super()._showdata()
        print(f"Experience = {self.exp}")
        print(f"Skill = {self.skill}")

    def __str__(self):
        return (super().__str__() + f"Experience = {self.exp} \nSkill = {self.skill}")