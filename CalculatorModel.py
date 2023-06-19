from math import sqrt

class CalculatorModel:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result
    
    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        try:
            result = num1 / num2
            self.history.append(f"{num1} / {num2} = {result}")
            return result
        except ZeroDivisionError:
            return "Ошибка: деление на 0"

    def square(self, num1):
        result = sqrt(num1)
        self.history.append(f"sqrt({num1}) = {result}")
        return result

    def power(self, num1, num2):
        result = num1 ** num2
        self.history.append(f"{num1} ^ {num2} = {result}")
        return result

    def get_history(self):
        return self.history