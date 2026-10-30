class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def get_salary(self):
        ''' Возвращает базовую зарплату сотрудника '''
        return self.salary
        
class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def get_salary(self):
        ''' Возвращает зарплату менеджера с учётом бонуса '''
        return self.salary + self.bonus
    
class Developer(Employee):
    def __init__(self, name: str, salary: float, program_language: str):
        super().__init__(name, salary)
        self.program_language = program_language
        
    def get_salary(self):
        ''' Вовзращает зарплату разработчика с учетом премии за язык программирования '''
        if self.program_language == 'Python':
            return self.salary + 5000
        elif self.program_language == 'Java':
            return self.salary + 7000
        elif self.program_language == 'C++':
            return self.salary + 10000
        else:
            return self.salary
        
employee1 = Employee('Иван', 50000)
manager1 = Manager('Мария', 70000, 15000)
developer1 = Developer('Алексей', 60000, 'Python')
print(f'зарплата сотрудника: {employee1.get_salary()}')
print(f'зарплата менеджера: {manager1.get_salary()}')
print(f'зарплата разработчика: {developer1.get_salary()}')