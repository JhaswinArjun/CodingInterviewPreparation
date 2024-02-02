# Problem 1: Find last digit in a number.
print('Problem 1: Find last digit in a number.')
"""
You are given two integer numbers, the base a and the index b. You have to find the last digit of ab.
Example 1:

Input:
a = "3", b = "10"
Output:
9
Explanation:
3**10 = 59049. Last digit is 9.
Example 2:

Input:
a = "6", b = "2"
Output:
6
Explanation:
6**2 = 36. Last digit is 6."""

# Method 1: Using String.
print('Method 1: Using String.')
def last_digit_using_string(a,b):
    return int(str(int(a) ** int(b))[-1]);

print(last_digit_using_string("3","10"));
print(last_digit_using_string("6","2"));

# Method 2 : Using modulus
print('Method 2 : Using modulus.')
def last_digit_using_modulus(a,b):
    return (int(a) ** int(b)) % 10

print(last_digit_using_modulus("3","10"));
print(last_digit_using_modulus("6","2"));

# Problem 2: Find first and last digits of a number.
print('Problem 2: Find first and last digits of a number.')

"""
Given a number to find the first and last digit of a number.
Examples: 

Input : 12345 
Output : First digit: 1
         last digit : 5

Input : 98562
Output : First digit: 9
         last digit : 2
"""
# Method 1: Number with loop.
print("Method 1: Number with loop.")
def get_last_digit(number):
    return number % 10;
def get_first_digit(number):
    while number >= 10:
        number /= 10
    return int(number)
def find_first_last_digit(number):
    return f"Last Digit: {get_last_digit(number)}, First digit: {get_first_digit(number)}"
print(find_first_last_digit(12345));
print(find_first_last_digit(98562));
