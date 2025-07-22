"""
calculator.py - Basic Calculator Functions

FUNCTIONALITY OVERVIEW:
This module implements a simple Calculator class that performs basic arithmetic operations
and maintains a history of all calculations performed. The calculator supports:
- Addition, subtraction, multiplication, division
- Exponentiation (power operations)  
- Calculation history tracking and management

WHAT TO REVIEW:
- Code structure and organization
- Error handling approaches
- Readability

This serves as the baseline implementation before modifications are made in other branches.
"""

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    # NEW FEATURE: Advanced operations
    def sqrt(self,x):
        import math
        r=math.sqrt(x)
        self.history.append(f"sqrt({x}) = {r}")
        return r
    
    def log(self,x,base=10):
        import math
        if base==10:r=math.log10(x)
        else:r=math.log(x,base)
        self.history.append(f"log_{base}({x}) = {r}")
        return r
    
    def factorial(self,n):
        if n<0:raise ValueError("Negative numbers not allowed")
        result=1
        for i in range(1,n+1):result*=i
        self.history.append(f"{n}! = {result}")
        return result
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    print(f"sqrt(16) = {calc.sqrt(16)}")
    print(f"5! = {calc.factorial(5)}")