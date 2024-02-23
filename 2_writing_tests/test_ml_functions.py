# test_ml_functions.py
import pytest
import allure

from scipy import stats
import numpy as np

from ml_functions import mean, median, mode

# Function to calculate the product of a number and elements of a list
def calculate_product(number, lst):
    return [number * x for x in lst]

# Test case using parametrize with a list as one of the parameters
@pytest.mark.parametrize("number, lst, expected_result", [
    (2, [1, 2, 3], [2, 4, 6]),        # Test case 1: number=2, lst=[1, 2, 3], expected_result=[2, 4, 6]
    (3, [4, 5, 6], [12, 15, 18]),     # Test case 2: number=3, lst=[4, 5, 6], expected_result=[12, 15, 18]
    (0, [7, 8, 9], [0, 0, 0]),        # Test case 3: number=0, lst=[7, 8, 9], expected_result=[0, 0, 0]
    (-1, [-1, -2, -3], [1, 2, 3])     # Test case 4: number=-1, lst=[-1, -2, -3], expected_result=[1, 2, 3]
])
def test_calculate_product(number, lst, expected_result):
    assert calculate_product(number, lst) == expected_result

# Importing the mean function from SciPy library
from scipy.stats import describe

# Test function to calculate the sum of three numbers
def calculate_sum(a, b, c):
    return a + b + c

# Test case using parametrize with three parameters per entry
@pytest.mark.parametrize("a, b, c, expected_sum", [
    (1, 2, 3, 6),   # Test case 1: a=1, b=2, c=3, expected_sum=6
    (4, 5, 6, 15),  # Test case 2: a=4, b=5, c=6, expected_sum=15
    (7, 8, 9, 24)   # Test case 3: a=7, b=8, c=9, expected_sum=24
])
def test_calculate_sum(a, b, c, expected_sum):
    assert calculate_sum(a, b, c) == expected_sum

@allure.feature("ML Functions Tests")
@allure.title("Test of Mean Function")
@allure.description("Import the function calculation the mean value from a list of ints from SciPy library.")
@pytest.mark.parametrize("input_values, expected_output", [
                        ([1, 2, 3], 2),
                        ([3, 3, 3], 3),
                        ([2, 2, 2], 2)
])
# @pytest.mark.parametrize("input_values, expected_output", [(1, 2)])
def test_mean(input_values, expected_output):
    computed_mean = mean(input_values)

    # Attach additional information to the test report
    allure.attach(str(input_values), name="Test Data")
    allure.attach(str(expected_output), name="Expected Mean")
    allure.attach(str(computed_mean), name="Computed Mean")

    assert computed_mean == expected_output


# Test function for testing normality
@pytest.mark.parametrize("data", [
    np.random.normal(0, 1, 100),  # Normal distribution
    np.random.normal(0, 1, 100),  # Normal distribution
    np.random.normal(0, 1, 100)   # Normal distribution
])
def test_normality(data):
    _, p_value = stats.normaltest(data)
    assert p_value > 0.05  # Null hypothesis: data is drawn from a normal distribution


# Test function for testing t-test
def test_ttest():
    # Generating two samples from normal distributions with identical means
    sample1 = np.random.normal(0, 1, 100)
    sample2 = np.random.normal(0, 1, 100)
    _, p_value = stats.ttest_ind(sample1, sample2)
    assert p_value > 0.05  # Null hypothesis: means of two samples are equal


# Test function for testing chi-square test
def test_chisquare():
    observed = np.array([25, 25, 25, 25])  # Observed frequencies
    expected = np.array([25, 25, 25, 25])  # Expected frequencies
    _, p_value = stats.chisquare(observed, expected)
    assert p_value > 0.05  # Null hypothesis: observed and expected frequencies are equal


# Test function for testing correlation
def test_correlation():
    x = np.random.normal(0, 1, 100)
    y = np.random.normal(0, 1, 100)
    corr_coef, p_value = stats.pearsonr(x, y)
    assert np.abs(corr_coef) < 0.5  # Null hypothesis: no correlation


if __name__ == "__main__":
    pytest.main()

