from Preprocess import Preprocess
import csv
import pandas as pd
from read_dataset import DataSet


def main():

    dataFrame = pd.read_csv('datasets1.csv')

    for index, row in dataFrame.iterrows():
        preprocc = Preprocess(row['FileContent'])
        dataFrame._set_value(index,'FileContent',preprocc.text_preProcess())
    dataFrame.to_csv('datasets1.csv',sep='\t')


# DataFrame2 = dataFrame.set_index("Label",drop=False)
# print(DataFrame2.loc['graphical','File'])
# preprocc = Preprocess(DataFrame2.loc['graphical','File'])
# DataFrame2['graphical','File'] = preprocc.text_preProcess()
# DataFrame2.insert('grapical','File',)


if __name__ == '__main__':
    main()
