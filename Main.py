from CalculatorModel import CalculatorModel
from CalculatorPresenter import CalculatorPresenter
from CalculatorView import CalculatorView

model = CalculatorModel()
view = CalculatorView()
presenter = CalculatorPresenter(model, view)
presenter.run()