if __name__ == "__main__":
    print("This script isn't suppoused to be executed seperatly!")

if __name__ == "alphaWorker":



    import openpyxl as pyxl
    from openpyxl import Workbook

    class AlphaWorker():

        def __init__(self):
            self._dataBase = pyxl.load_workbook("./resources/dataBase.xlsx")
        def populate(self, charset):
            pass
    

    pass
