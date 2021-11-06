# position, name, age, level, salary

se1 = ["Software Engineer", "Lionel", 20, "junior", 5000]
se2 = ['Software Engineer', 'Brendy', 25, 'senior', 10000]
d1= ['Data Scientist', 'Benny']

def code(se):
    print(f"{se[1]} is writing code...")

code(se2)
code(d1)

# class
class SoftwareEngineer:

    # class attribute
    alias = "keyboard wizard"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age={self.age}, level = {self.level}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age <30:
            return 7000
        return 9000

# instance

se1 = SoftwareEngineer("Lionel", 20, "junior", 5000)
se2 = SoftwareEngineer('Brendy', 25, 'senior', 10000)
se3 = SoftwareEngineer('Brendy', 25, 'senior', 10000)

se1.code()
se2.code()
se1.code_in_language('Python')
se2.code_in_language('C++')

print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))