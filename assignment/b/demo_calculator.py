# demo_calculator.py

from calculator import Calculator

def main() -> None:
    calc = Calculator()
    
    # Demonstrate add
    result_add = calc.add(3.0, 4.0)
    print(f"3.0 + 4.0 = {result_add}")
    
    # Demonstrate subtract
    result_subtract = calc.subtract(10.0, 5.0)
    print(f"10.0 - 5.0 = {result_subtract}")
    
    # Demonstrate multiply
    result_multiply = calc.multiply(2.0, 3.0)
    print(f"2.0 * 3.0 = {result_multiply}")
    
    # Demonstrate divide
    result_divide = calc.divide(10.0, 2.0)
    print(f"10.0 / 2.0 = {result_divide}")
    
    # Test divide by zero
    try:
        calc.divide(10.0, 0.0)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
