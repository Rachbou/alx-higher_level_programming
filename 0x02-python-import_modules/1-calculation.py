#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.sub(a, b)}")
    print(f"{a} * {b} = {calculator.mul(a, b)}")
    print(f"{a} / {b} = {calculator.div(a, b)}")
