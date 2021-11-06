# position, name, age, level, salary

se1 = ["Software Engineer", "Lionel", 20, "junior", 5000]
se2 = ['Software Engineer', 'Brendy', 25, 'senior', 10000]

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

# instance
se1 = SoftwareEngineer("Lionel", 20, "junior", 5000)
print(se1.name, se1.age)
print(se1.alias)
se2 = SoftwareEngineer("Brendy", 25, "senior", 10000)
print(SoftwareEngineer.alias)

# Recap
# create a class (blueprint)
# create an instance (object)
# class vs instance
# instance attributes
