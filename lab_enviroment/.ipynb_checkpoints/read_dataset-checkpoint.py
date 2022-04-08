import pandas as pd

class DataSet:

    def __init__(self):
        filename = "JabRef_betterFormat.xlsx"
        self.file = pd.read_excel(filename)

    def getData(self):
        return self.file

