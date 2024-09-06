from classAccounting import Accounting
from classProgramming import Programmer
from classSale import Sale


# Output 
print("_________________________________________")

account = Accounting("Thomas", 52000,5)
print(account.__str__())
print("_________________________________________")

programmer = Programmer("Shell",122222, 10, 'Game Development')
print(programmer.__str__())
print("_________________________________________")

sale = Sale("Hella",500, 'Chiange Mai')
print(sale.__str__())
print("_________________________________________")

print(account._getIncome(bonus=500))