#mae demagante

import pytest
"""
class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a+b
        
calc = Calculator("Calc 1")

def test_lab4():
    print("This calculator's name is " + calc.name)
    
    #Changes calculator's name
    calc.name = "Calc 2"
    print("This calculator's name is " + calc.name)
    print(calc.add(1,1))
    
    assert True
    
"""


class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self,a,b):
        return a+b
        
    def subtract(self,a,b)
        return a-b
        
    def multiply(self, a, b)
       return a * b      

#calling purposes
calc = Calculator("calc")

@p  ytest.fixture
def base_calculator():
    return Calculator ("Base Calculator")
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_subtract():
    assert.subtract(0,0) == 0
    assert.subtract(-2,-4) == 2
    assert.subtract(3,1) == 2
    assert.subtract(-2,1) == -3
    
def test_multiply():
    assert.multiply(0,1) == 0 
    assert.multiply(1,4) == 4
    assert.multiply(-3,2) == -6
    assert.multiply(-2,-1) == 2
    
    