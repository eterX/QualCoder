# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_import.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Import(object):
    def setupUi(self, Dialog_Import):
        Dialog_Import.setObjectName("Dialog_Import")
        Dialog_Import.resize(946, 579)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_Import.sizePolicy().hasHeightForWidth())
        Dialog_Import.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_Import)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Import)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Import)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 1)
        self.label_msg = QtWidgets.QLabel(Dialog_Import)
        self.label_msg.setObjectName("label_msg")
        self.gridLayout.addWidget(self.label_msg, 5, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog_Import)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 160))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_delimiter = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_delimiter.setGeometry(QtCore.QRect(170, 30, 71, 31))
        self.lineEdit_delimiter.setObjectName("lineEdit_delimiter")
        self.label_delimiter = QtWidgets.QLabel(self.groupBox)
        self.label_delimiter.setGeometry(QtCore.QRect(10, 36, 141, 21))
        self.label_delimiter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_delimiter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_delimiter.setObjectName("label_delimiter")
        self.label_quotefmt = QtWidgets.QLabel(self.groupBox)
        self.label_quotefmt.setGeometry(QtCore.QRect(310, 30, 211, 31))
        self.label_quotefmt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_quotefmt.setObjectName("label_quotefmt")
        self.comboBox_quote = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_quote.setGeometry(QtCore.QRect(530, 30, 151, 31))
        self.comboBox_quote.setObjectName("comboBox_quote")
        self.comboBox_quote.addItem("")
        self.comboBox_quote.addItem("")
        self.comboBox_quote.addItem("")
        self.label_information = QtWidgets.QLabel(self.groupBox)
        self.label_information.setGeometry(QtCore.QRect(10, 100, 901, 51))
        self.label_information.setWordWrap(True)
        self.label_information.setObjectName("label_information")
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)

        self.retranslateUi(Dialog_Import)
        self.buttonBox.accepted.connect(Dialog_Import.accept)
        self.buttonBox.rejected.connect(Dialog_Import.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Import)
        Dialog_Import.setTabOrder(self.lineEdit_delimiter, self.comboBox_quote)
        Dialog_Import.setTabOrder(self.comboBox_quote, self.tableWidget)
        Dialog_Import.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, Dialog_Import):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Import.setWindowTitle(_translate("Dialog_Import", "Import"))
        self.label_msg.setText(_translate("Dialog_Import", "."))
        self.groupBox.setTitle(_translate("Dialog_Import", "Survey Import Options"))
        self.lineEdit_delimiter.setToolTip(_translate("Dialog_Import", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_delimiter.setText(_translate("Dialog_Import", ","))
        self.label_delimiter.setToolTip(_translate("Dialog_Import", "<html><head/><body><p>Delimiter must be a single character.</p><p>Enter \'ta\' for \'tab\'</p></body></html>"))
        self.label_delimiter.setText(_translate("Dialog_Import", "Delimiter:"))
        self.label_quotefmt.setText(_translate("Dialog_Import", "Quote format:"))
        self.comboBox_quote.setToolTip(_translate("Dialog_Import", "<html><head/><body><p>NONE 123, abc</p><p>MINIMAL 123, &quot;abc&quot;</p><p>ALL &quot;123&quot;, &quot;abc&quot;</p><p><br/></p></body></html>"))
        self.comboBox_quote.setItemText(0, _translate("Dialog_Import", "NONE"))
        self.comboBox_quote.setItemText(1, _translate("Dialog_Import", "MINIMAL"))
        self.comboBox_quote.setItemText(2, _translate("Dialog_Import", "ALL"))
        self.label_information.setText(_translate("Dialog_Import", "Changes made on the top row will override any user changes to field names and field types below."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Import = QtWidgets.QDialog()
    ui = Ui_Dialog_Import()
    ui.setupUi(Dialog_Import)
    Dialog_Import.show()
    sys.exit(app.exec_())

