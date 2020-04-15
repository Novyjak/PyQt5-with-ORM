from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QTableWidgetItem, QTableWidget
from AddData import DataAdder
from DataRemover import DataRemover
import Database



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window" # název okna
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 600  # proměnné použité pro velikost okna


        self.initui()

    def initui(self):

        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        # v hlavním okně (QMainWindow) existuje více míst, které se dají měnit, jako například i toolbar
        # proto se musí deklarovat, do které části vkládáme

        grid = QGridLayout() # grid slouží k rovnoměrnému rozmístění, které zůstává i při změně velikosti okna

        button1 = QPushButton("View Database", self) # tvorba tlačítka
        button1.clicked.connect(self.showdata) # pokud bychom chtěli do funkce něco vložit, tak se musí použít "...connect(lambda: self.example(input))"

        grid.addWidget(button1,0,0) # přidáváme tlačítko do gridu na pozici [0,0], grid si sám rozděluje okno podle počtu vložených Widgetů

        centralwidget.setLayout(grid) # je nutné oknu oznámit, že se podle gridu musí rozložit

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()  # bez show() by se spustil pouze proces, ale okno by se nezobrazilo

    def showdata(self):

        newcentralwidget = QWidget()
        self.setCentralWidget(newcentralwidget) # nastavení nového rozpoložení okna, druhá možnost by byla zavřít staré okno a otevřít nové
        grid = QGridLayout()

        addButton = QPushButton("Add",self)
        addButton.clicked.connect(self.adddata) # otevře nové okno, kde se dají vložit nová data do databáze

        removeButton = QPushButton("Remove",self)
        removeButton.clicked.connect(self.removedata) # otevře nové okno, kde se dají vymazat data z databáze


        refreshButton = QPushButton("Refresh",self)
        refreshButton.clicked.connect(self.pressrefresh)

        self.tablewidget = QTableWidget() # zobrazení tabulky
        self.pressrefresh() # funkce sloužící pro obnovení tabulky na aktuální informace
        # použita zde pro první nahrání dat do tabulky


        grid.addWidget(self.tablewidget,0,0,4,4)
        grid.addWidget(addButton, 0, 5)
        grid.addWidget(removeButton, 1, 5)
        grid.addWidget(refreshButton, 2, 5)

        newcentralwidget.setLayout(grid)

    def pressrefresh(self): # funkce sloužící pro obnovení tabulky na aktuální informace
        self.tablewidget.setSortingEnabled(False)

        self.tablewidget.setRowCount(Database.number_of_rows())
        self.tablewidget.setColumnCount(4)
        itemlist = Database.query_all()

        for i in range(Database.number_of_rows()):
            for j in range(4):
                self.tablewidget.setItem(i, j, QTableWidgetItem(str(itemlist[i][j])))

        self.tablewidget.setSortingEnabled(True)

    def adddata(self):
        self.next = DataAdder()

    def removedata(self):
        self.next = DataRemover()

