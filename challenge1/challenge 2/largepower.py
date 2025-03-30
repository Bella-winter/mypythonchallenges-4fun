#control flows in python
def large_power(base, exponent):
        # Calculate the result of base to the power of exponent
    result = base ** exponent

 # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
    ## Example usage
print(large_power(10, 3))  # Output: True (10^3 = 1000)
print(large_power(5, 3,))   # Output: False (5^3 = 125)
print (large_power(7, 10)) # Output: True (7^10 = 282475249)
print (large_power(20, 3)) # Output: True (20^3 = 8000)


