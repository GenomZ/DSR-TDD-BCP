# The "Power of Ten - NASA/JPL Coding Guidelines" provide a set of coding rules and best practices
# for software development, particularly in safety-critical or high-reliability systems.
# These guidelines are designed to enhance code readability, maintainability, and reliability.

# 1. Limit Line Length: Keep lines of code relatively short for readability.

# Bad example
long_variable_name = calculate_some_really_long_function_name(argument1, argument2, argument3, argument4)

# Good example
result = calculate_short_function(arg1, arg2)

# 2. Limit Function Length: Keep functions short and focused.

# Bad example
def complex_function(arg1, arg2, arg3):
    # 50 lines of code here
    ...

# Good example
def simple_function(arg1, arg2):
    # A few lines of code here
    ...


# 3. Limit File Length: Keep files reasonably small and focused.

# Bad example: LargeFile.py

# Good example: SmallFile1.py, SmallFile2.py, etc.


# 4. Limit Routine Length: Similar to function length, keep routines (methods) short.

# Bad example
class SomeClass:
    def long_routine(self, arg1, arg2):
        # 50 lines of code here
        ...

# Good example
class SomeClass:
    def short_routine(self, arg1, arg2):
        # A few lines of code here
        ...

# 5. Limit Variable Scope: Minimize the scope of variables.

# Bad example
def some_function():
    global some_var
    some_var = 10
    ...

# Good example
def some_function():
    some_var = 10
    ...

# 6. Use Constants for Magic Numbers: Avoid magic numbers; use named constants.

# Bad example
if x > 86400:
    ...

# Good example
SECONDS_IN_DAY = 86400
if x > SECONDS_IN_DAY:
    ...


# 7. Limit Data Hiding: Don't use unnecessary access specifiers in classes.

# Bad example
class SomeClass:
    def __init__(self):
        self.__private_var = 10
    def get_private_var(self):
        return self.__private_var

# Good example
class SomeClass:
    def __init__(self):
        self.private_var = 10

# 8. Avoid Using Macros: In Python, this translates to avoiding global constants or variables.

# Bad example
PI = 3.14159

# Good example
import math
pi = math.pi

# 9. Avoid Compound Statements: Keep statements simple and separate.

# Bad example
if condition1 and condition2:
    ...

# Good example
if condition1:
    if condition2:
        ...


# 10. Avoid Negative Logic: Write conditions in positive form when possible.

# Bad example
if not is_invalid:
    ...

# Good example
if is_valid:
    ...


# SOLID
# Single Responsibility Principle (SRP):
class UserManager:
    def __init__(self):
        self.db = Database()

    def add_user(self, user):
        self.db.insert(user)

    def remove_user(self, user_id):
        self.db.delete(user_id)


class Database:
    def insert(self, user):
        # Logic to insert user into database

    def delete(self, user_id):
        # Logic to delete user from database

# 2.Open/Closed Principle (OCP):

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
            self.width = width
            self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# 3. Liskov Substitution Principle (LSP):

class Bird:
    def fly(self):
        pass

class Duck(Bird):
    def fly(self):
        print("Duck flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

# 4. Interface Segregation Principle (ISP):

class Printer:
    def print(self, document):
        pass


class Scanner:
    def scan(self, document):
        pass


class Photocopier(Printer, Scanner):
    pass


class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        # Logic to print document

    def scan(self, document):
        # Logic to scan document


# 5. Dependency Inversion Principle (DIP):

class Database:
    def get_data(self):
        pass

class DataManager:
    def __init__(self, database):
        self.database = database
    def process_data(self):
        data = self.database.get_data()
        # Process data

        db = Database()
        data_manager = DataManager(db)
