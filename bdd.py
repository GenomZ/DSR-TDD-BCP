# Step definitions
from pytest_bdd import given, when, then

@given("I have two numbers <a> and <b>")
def numbers(a, b):
    return int(a), int(b)

@when("I add them together")
def add_numbers(numbers):
    return numbers[0] + numbers[1]

@then("I should get the result as <result>")
def result(numbers, result):
    assert add_numbers(numbers) == int(result)