class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}")

class Payroll(Employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.base_salary + self.bonus

    def generate_pay_slip(self):
        self.display_details()
        print(f"Base Salary: ${self.base_salary}")
        print(f"Bonus: ${self.bonus}")
        print(f"Total Net Pay: ${self.calculate_total_salary()}")

# Create object of derived class
emp_payroll = Payroll(101, "Alice Smith", 50000, 5000)
emp_payroll.generate_pay_slip()