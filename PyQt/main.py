import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BMI Rechner")
        self.ui.calculat.clicked.connect(self.button_on_click)
        self.ui.result.hide()
        self.ui.label_result.hide()
    def button_on_click(self):
        weight = float(self.ui.weight.value())
        height = float(self.ui.height.value())
        if height != 0:
            bmi = round(weight / (height ** 2),2)
        else: result = "ERROR"
        result = str(bmi)
        print(result)
        self.ui.result.setText(result)
        self.ui.result.show()
        self.ui.label_result.show()
window = MainWindow()
window.show()
sys.exit(app.exec_())