


if __name__ == "__main__":
    import install
    import alphaWorker

    import pyforms
    from pyforms import BaseWidget
    from pyforms.controls import ControlText
    from pyforms.controls import ControlButton
    from pyforms.controls import ControlCombo

    class MainWindow(BaseWidget):

        def __init__(self):
            super(MainWindow, self).__init__("Calculator App")

            self._firstChar = ControlText("First Character")
            self._secondChar = ControlText("Second Character")
            self._submitAlphabetButton = ControlButton("Submit alphabet")

            self._currentAlphabet = ControlCombo("CurrentAlphabet")
            self._firstOperand = ControlText("First Operand")
            self._secondOperamd = ControlText("SecondOperand")
            self._calcButton = ControlButton("Calculate")

    pyforms.start_app(MainWindow)


