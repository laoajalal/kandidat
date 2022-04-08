# Feature selection
Date: 10-02/2021  
Sources:  
- [Medium: A feature selection tool for ML in python](https://towardsdatascience.com/a-feature-selection-tool-for-machine-learning-in-python-b64dd23710f0)
- [Feature selection in python with scikit-learn](https://machinelearningmastery.com/feature-selection-in-python-with-scikit-learn/)
- [Scikit-learn: Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html)
- [An introduction to variable and feature selection (pdf)](http://jmlr.csail.mit.edu/papers/volume3/guyon03a/guyon03a.pdf)
Backlink: [supervised-learning-310121-2011](supervised-learning-310121-2011.md)  

---
#### What is a feature?
A feature is an individual measurable property or characteristic of a phenomenon
being observed.
Features are structured as strings and graphs, they are typically numeric.
The selection for features is a crucial step for effective algorithms in pattern
recognition, classification and regression.

A set of numeric features are usually described by a feature vector.

#### Feature selection
Is an automatic process that automatically selects features in the given dataset 
to contribute towards the prediction output that is desired.

To many unrelated features in the dataset leads to decreased accuracy of the 
model. 

#### Desired result 
The desired benefits from performing feature selection is:
- __Reduced overfitting__, less redundant data means less noise.
- __Improved accuracy__, less misleading data in which results in improved  
  accuracy for the modeling.
- __Reduces training time__, less data to train.

#### Methods in Scikit-learn
Recursive Feature Selection Elimination
Feature Importance
Univariate Selection
Principal Component Analysis


----
Tags: @Machine-Learning @feature-selection
