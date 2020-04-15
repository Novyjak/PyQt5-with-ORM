from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox
import Database

class DataRemover(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 200
        self.left = 500
        self.width = 200
        self.height = 200

        self.initui()

    def initui(self):
        grid = QGridLayout()
        grid.setSpacing(5)

        infotext = QLabel("Input item, you want removed, precise name as in database:")
        itemlabel = QLabel("Item:")

        iteminput = QLineEdit()

        confirmButton = QPushButton("Confirm", self)
        closeButton = QPushButton("Close", self)

        closeButton.clicked.connect(self.close)
        confirmButton.clicked.connect(lambda: self.removeitem(iteminput.text()))

        grid.addWidget(infotext, 0, 0)
        grid.addWidget(itemlabel, 1, 0)
        grid.addWidget(iteminput, 1, 1)
        grid.addWidget(confirmButton, 2, 0)
        grid.addWidget(closeButton, 2, 1)

        self.setLayout(grid)

        self.show()

    def removeitem(self, item):
        if item == "" :
            message = QMessageBox.about(self, "Warning", "There is no input in ITEM field.")  # oznamovací okno bez funkce
        else:
            if Database.query_item(str(item)) is True: # nejdříve zkontroluje, jestli je item v databázi
                message = QMessageBox.question(self, "Warning", "Are you sure you want to delete {item}".format(item = str(item))
                                               , QMessageBox.Yes | QMessageBox.No) # oznamovací okno s více funkcemi, pamatuje si, na co bylo kliknuto
                if message == QMessageBox.Yes:
                    Database.delete_item(str(item))
                    self.close()
            else:
                message = QMessageBox.about(self, "Warning", "There is no item named {item} in database.".format(item = str(item)))