class employer:
    payroll = 0
    def calculate_payroll(self):
        pass

class hourlyemployer(employer):
    hourlyRate = 0
    def __init__(self, rate):
        self.hourlyRate = rate
    def calculate_payroll(self):
        self.payroll= 20.8 * 8 * self.hourlyRate
    def print_info(self):
        print(self.payroll)

class fixedTermemployer(employer):
    salary = 0
    def __init__(self, salary):
        self.salary = salary
    def calculate_payroll(self):
        self.payroll=self.salary
    def print_info(self):
        print(self.payroll)


Vasya = hourlyemployer(int(input("Ввидите почасовую ставку: ")))
Vasya.calculate_payroll()
Vasya.print_info()
Pit = fixedTermemployer(int(input("Ввидите фиксированную зарплату: ")))
Pit.calculate_payroll()
Pit.print_info()
