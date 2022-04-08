from Preprocess import Preprocess
from DataCollecterCSV import collectJabRef

import pandas as pd
import Testing as test

def main():
    dataSet = 'dataset.csv'

    collectJabRef(dataSet) ## Laddar all data till CVS-fil, data ej ren
    dataFrame = pd.read_csv(dataSet)
    Preprocess().preProcess(dataFrame,dataSet)
    test.Naive_Bayes_MultiNominal(dataFrame)
    test.SVM_RBF_kernel(dataFrame)
    test.SVM_poly(dataFrame,2)
    test.SVM_linear(dataFrame)
    test.MaxEnt(dataFrame)
if __name__ == '__main__':
    main()
