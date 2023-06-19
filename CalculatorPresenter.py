class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
 
    def run(self):
        while True:
            operator, num1, num2 = self.view.get_input()
            if operator == "+":
                result = self.model.add(num1, num2)
            elif operator == "*":
                result = self.model.multiply(num1, num2)
            elif operator == "/":
                result = self.model.divide(num1, num2)
            elif operator == "sqrt":
                result = self.model.square(num1)
            elif operator == "pow":
                result = self.model.power(num1, num2)
            else:
                result = "Ошибка: неправильный знак (операция)"
            self.view.display_result(result)
            self.view.display_history(self.model.get_history())
