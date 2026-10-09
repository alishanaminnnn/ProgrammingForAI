def gcd(a, b):
    # Use the Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate LCM using GCD
    return (a * b) // gcd(a, b)

# Test with a = 12 and b = 18
a = 12
b = 18

# Print GCD and LCM
print("GCD =", gcd(a, b))
print("LCM =", lcm(a, b))
