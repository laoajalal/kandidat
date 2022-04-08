# Supervised-Learning
Date: 31-01/2021  
Sources: https://en.wikipedia.org/wiki/Supervised_learning  
Backlink: [machine-learning](machine-learning)  

---
#### What is Supervised Learning?
Is the task of learning a function that maps an input to an output. 
Learning from labeled training data, then from the input object (typically a 
vector) to a desired output value (typically called supervisory signal).
The supervised learning algorithm analyzes the training data to then create a 
function that will be used to mapping new examples.

#### The steps from wiki for solving a Supervised learning problem
1. Determine the type of training examples.  
   *In our case it will be mapping the dependencies of source code.*
2. Gather a training set that represents the real-world use data.
3. [Feature selection](feature-selection-100221-2210) for the learned function.  
   The accuracy of the learned function depends strongly on how the input  
   object is represented. It's typically transformed into a feature vector, which
   contain a number of features that are descriptive of the object.  
   - The number of features should not to be large, to avoid the curse of 
     dimensionality.
   - The number of features should not to be small, to be able to accurately  
     predict the output.
4. Determine the structure of the learned function and corresponding learning  
   algorithms. E.g. support vector machines or decision trees
5. Complete the design. Have a validation set or cross-validation
6. Evaluate the accuracy of the learned function.

#### Algorithms
- Support vector machines
- Linear regression
- Logistic regression
- Naive Bayes
- Linear discriminant analysis
- Decision trees
- K-nearest neighbor algorithm
- Neural networks (multilayer perceptron)
- Similarity learning

----
