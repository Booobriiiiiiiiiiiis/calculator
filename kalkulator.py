# Form implementation generated from reading ui file 'kalkulator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pervoeclagaemoemeymenshaemoeperuimnozhiteldelimoe = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pervoeclagaemoemeymenshaemoeperuimnozhiteldelimoe.setGeometry(QtCore.QRect(20, 20, 31, 51))
        self.pervoeclagaemoemeymenshaemoeperuimnozhiteldelimoe.setObjectName("pervoeclagaemoemeymenshaemoeperuimnozhiteldelimoe")
        self.vtoroeclagaemoevuchitaemoevtoroimnozhiteldelitel = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.vtoroeclagaemoevuchitaemoevtoroimnozhiteldelitel.setGeometry(QtCore.QRect(100, 20, 31, 51))
        self.vtoroeclagaemoevuchitaemoevtoroimnozhiteldelitel.setObjectName("vtoroeclagaemoevuchitaemoevtoroimnozhiteldelitel")
        self.plusminuspazdelitumnozhit = QtWidgets.QLabel(parent=self.centralwidget)
        self.plusminuspazdelitumnozhit.setGeometry(QtCore.QRect(60, 20, 31, 51))
        self.plusminuspazdelitumnozhit.setObjectName("plusminuspazdelitumnozhit")
        self.cummaraznostproizvedeniechastnoe = QtWidgets.QLabel(parent=self.centralwidget)
        self.cummaraznostproizvedeniechastnoe.setGeometry(QtCore.QRect(190, 19, 31, 70))
        self.cummaraznostproizvedeniechastnoe.setObjectName("cummaraznostproizvedeniechastnoe")
        self.pavno = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pavno.setGeometry(QtCore.QRect(130, 29, 56, 30))
        self.pavno.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.pavno.setObjectName("pavno")
        self.pavno.clicked.connect(self.samostoyatelnui_def_class_pod_nim_hodit_vu_prosto_ne_zamechaite)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plusminuspazdelitumnozhit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">+</span></p></body></html>"))
        self.cummaraznostproizvedeniechastnoe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt;\">0</span></p></body></html>"))
        self.pavno.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">=</span></p></body></html>"))
        self.pavno.setText(_translate("MainWindow", "="))
    def samostoyatelnui_def_class_pod_nim_hodit_vu_prosto_ne_zamechaite(self):
        samostoyatelnaya_a_vu_prosto_ne_zamechaite = int(self.pervoeclagaemoemeymenshaemoeperuimnozhiteldelimoe.text())
        samostoyatelnaya_b_vu_prosto_ne_zamechaite = int(self.vtoroeclagaemoevuchitaemoevtoroimnozhiteldelitel.text())
        self.cummaraznostproizvedeniechastnoe.setText(str(samostoyatelnaya_a_vu_prosto_ne_zamechaite + samostoyatelnaya_b_vu_prosto_ne_zamechaite))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
