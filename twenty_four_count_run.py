import sys

from PyQt5.QtWidgets import QApplication

from twenty_four_count import subUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = subUi()
    myWin.show()
    sys.exit(app.exec_())