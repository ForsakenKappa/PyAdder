if __name__ == "__main__":
    print("This script isn't suppoused to be executed seperatly!")

if __name__ == "alphaWorker":

    import openpyxl as pyxl
    from openpyxl import Workbook

    class AlphaWorker():

        def __init__(self):
            self._dataBase = pyxl.load_workbook("./resources/dataBase.xlsx")
            self._activeWS = self._dataBase.active

        def appendCharset(self, charset):
            #Charset выглядит как массив из двух элементов, например ["чупапи","муняню"]
            for row in range(1, 9999):
                DBrow = self._activeWS[row]
                if len(DBrow) == 0:
                    self._activeWS.append(charset)

        def getCharset(self, row):
            charset = []
            DBrow = self._activeWS[row]
            for rowv in DBrow:
                charset.append(rowv.value)

        def deleteRow(self, row):
            self._activeWS.delete_rows(row)

    pass
