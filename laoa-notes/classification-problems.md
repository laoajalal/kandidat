# Classification problems
Instead of predicting our result in a continous manner which is done in regression problems, classification problems maps the result to a discrete output. 

**Example**
1. Decide if a Email is spam/ not spam
2. Tumor: Malignant / Benign?

These types are called binary classifciation problems. The more general type is multivariable classification problems where the output can contain more than 2 possible outputs.

Applying a linear regression to a classification problem usually does works bad. This due to the nature of these kinds of problems where the output should only range from 0 to 1 (for binary classifications). Instead, we want to create a hypothesis where it ranges from the values 0 <=h(x) <=1. These are called [Logistic Regressions](logistic-regression.md).


Powerpoint slide of good Text classification information : https://www.ke.tu-darmstadt.de/lehre/archiv/ss12/web-mining/wm-tm.pdf