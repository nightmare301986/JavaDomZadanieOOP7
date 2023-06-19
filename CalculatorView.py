import os

class CalculatorView:
    def get_input(self):
        operator = input("Введите операцию (+, *, /, sqrt, pow): ")
        if (operator != "sqrt") and (operator != "exit"):
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите второе число: "))
        elif operator == "sqrt":
            num1 = float(input("Введите число: ")) 
            num2 = 0 
        else:
            os._exit(os.EX_OK)
        return operator, num1, num2

    def display_result(self, result):
        print("Результат: ", result)

    def display_history(self, history):
        print("История операций:")
        for operation in history:
            print(operation)