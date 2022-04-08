# OnevsOne and One vs Rest
There are a lot of classification models that were designed to only classify binary ourcomes, typically the yes or no nature. For example, if a classifier is trained to identify fruits, it does not consider if it is a apple, orange etc.. it just answers the base question with a yes or no answer.

These classifiers are limited and often we want to describe data in terms of more than 2 outcomes. Maybe our classifiers about fruits should also output which fruit that is being identified. This problem becomes multidimensional.

Our project relies on mapping source code to a specific label. As project becomes large, there will more than often be more than 2 outcomes that the source code can map to. I have previously mentioned 2 different approaches, logisitc regression and support vector machines. These are binary and need to be extended to a multi-class classifier. 

## One vs Rest
 - Splits the multi-class classification problem into multiple binary classification problems. The binary classifier is then trained iterative. For example, identifying if the text article desribes soccer, hockey or tennis. One classifier can look like this: soccer vs (hockey and tennis), the secound: hockey vs (tennis and soccer) and third tennis vs (soccer and hockey). If analyzed we can see that for n different labels, we need to create n classifiers. 
 - As described above, we have to create n classifiers for n classes. This does not scale well when n becomes large and requires a lot of resources to maintain.

## One vs One
Like One vs Rest, One vs One also splits multiple classification problems to binary classification. The major difference is that one vs one splits the datasets into one dataset for each class versus every other class.

- Example: If we have 3 genres: Action, Comedy and Horror, the amount of datasets will be:
Action vs Comedy
Action vs Horror
Comedy vs Horror
- This can be calculated with the formula (#classes *(#classes - 1)) /2.

- This approach is suggested to be used with SVM and other kernal based algorithms.



