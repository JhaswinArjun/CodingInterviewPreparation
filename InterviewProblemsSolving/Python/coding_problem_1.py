"""
Beginners basic math probs - Find even or odd
Problem link : https://www.geeksforgeeks.org/problems/odd-or-even3618/1
To find whether the number is even or odd.
"""

# Method 1: Using modulus.
print("Method 1: Using modulus.");

def is_even_modulus(number):
    return number % 2 == 0;
# If true then it is even.
# If false then it is false.
print(is_even_modulus(6));
print(is_even_modulus(9));

# Method 2: Using binary.
print("Method 2: Using binary.");

# The main concept here is binary even numbers end with 0 so even & 1 is 0, odd numbers end with 1 so odd & 1 is 1.
def is_even_binary(number):
    return number & 1 == 0;
print(is_even_binary(6));
print(is_even_binary(9));

# Method 3: Using Bitwise Shift.
print('Method 3: Using Bitwise Shift.');
# Bitwise shift rule.
# For even numbers when we shift once right and once left the initial and final binary number remains the same.
# For odd numbers when we shift once right and once left the initial and final  binary number is different.
def is_even_bitwise(number):
    return number == (number >> 1) << 1 ;
print(is_even_bitwise(6));
print(is_even_bitwise(9));
