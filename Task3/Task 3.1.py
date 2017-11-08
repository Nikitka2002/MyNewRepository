class employee:
    payroll = 0
    def calculate_payroll(self):
        pass

class hourlyemployee(employee):
    hourlyRate = 0
    def __init__(self, rate):
        self.hourlyRate = rate
    def calculate_payroll(self):
        self.payroll= 20.8 * 8 * self.hourlyRate
    def print_info(self):
        print(self.payroll)

class fixedTermemployee(employee):
    salary = 0
    def __init__(self, salary):
        self.salary = salary
    def calculate_payroll(self):
        self.payroll=self.salary
    def print_info(self):
        print(self.payroll)


Vasya = hourlyemployee(2)
Vasya.calculate_payroll()
Vasya.print_info()
Pit = fixedTermemployee(2400)
Pit.calculate_payroll()
Pit.print_info()
