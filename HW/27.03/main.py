from PyQt6 import QtCore, QtGui, QtWidgets
from calculator_ui import Ui_Calculator

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addition)
        self.ui.pushButton_2.clicked.connect(self.subtraction)
        self.ui.pushButton_3.clicked.connect(self.multiplication)
        self.ui.pushButton_4.clicked.connect(self.division)

    def addition(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 + num2
        self.ui.label.setText(str(result))

    def subtraction(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 - num2
        self.ui.label.setText(str(result))

    def multiplication(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 * num2
        self.ui.label.setText(str(result))

    def division(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 / num2
        self.ui.label.setText(str(result))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
