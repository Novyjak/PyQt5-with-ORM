from PyQt5.QtWidgets import QDialog, QPushButton, QGridLayout, QLabel, QLineEdit, QMessageBox
import Database

class DataAdder(QDialog):
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

        infotext = QLabel("Input item, its quantity and price:")
        additem = QLabel("Item:")
        addquantity = QLabel("Quantity")
        addprice = QLabel("Price")

        iteminput = QLineEdit()
        quantityinput = QLineEdit()
        priceinput  = QLineEdit()

        confirmButton = QPushButton("Confirm",self)
        closeButton = QPushButton("Close",self)

        closeButton.clicked.connect(self.close)
        confirmButton.clicked.connect(lambda: self.additem(iteminput.text(), quantityinput.text(), priceinput.text()))

        grid.addWidget(infotext, 0, 0)
        grid.addWidget(additem, 1, 0)
        grid.addWidget(iteminput, 1, 1)
        grid.addWidget(addquantity, 2, 0)
        grid.addWidget(quantityinput, 2 , 1)
        grid.addWidget(addprice, 3, 0)
        grid.addWidget(priceinput, 3, 1)
        grid.addWidget(confirmButton, 4 , 0)
        grid.addWidget(closeButton, 4, 1)

        self.setLayout(grid)

        self.show()

    def additem(self, item, quantity, price):
        if item == "" :
            message = QMessageBox.about(self, "Warning", "There is no input in ITEM field.")

        elif quantity == "":
            message = QMessageBox.about(self, "Warning", "There is no input in QUANTITY field.")

        elif item == "":
            message = QMessageBox.about(self, "Warning", "There is no input in PRICE field.")

        else:
            try:
                int(quantity)
                try:
                    float(price)
                    Database.add_item(item, quantity, price)
                    self.close()
                except ValueError:
                    message = QMessageBox.about(self, "Warning", "PRICE must be a number")
            except ValueError:
                message = QMessageBox.about(self, "Warning", "QUANTITY must be a number")

