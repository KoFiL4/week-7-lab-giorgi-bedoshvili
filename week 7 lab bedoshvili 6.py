# Week 7 Lab Bedoshvili 5.py
# Script to display both original and obfuscated code

def show_original():
    original_code = """def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))"""
    return original_code

def show_obfuscated():
    obfuscated_code = """def a(b):
    if b==0 or b==1:
        return 1
    else:
        return b*a(b-1)

print("Factorial of 5 is:", a(5))"""
    return obfuscated_code

if __name__ == "__main__":
    print("=== Original Code (week 7 lab bedoshvili 3.py) ===")
    print(show_original())
    print("\n=== Obfuscated Code (week 7 lab bedoshvili 4.py) ===")
    print(show_obfuscated())
