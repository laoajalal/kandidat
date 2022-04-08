# Möjliga val av algoritmer

1. [Naive Bayes](Naive-bayes.md)
2. [Multinominal logistic regression](Multinominal-logistic-regression.md)
3. [Support-vector machines](SVM.md)
4. [K-nearest neigbours](k-nearest.md)
5. [Decision trees](Decision-Trees.md)
6. [Logistic Regression with extensions (one vs all, one vs one)](Logistic-regression-with-extensions.md)


## Motivation
Our project can be generlized to a multiclass classification problem, where we train a classifier to map different classes to respective label. To map class-files, the text has to be pre-processed, assuring that as much as relevant information is passed to the ML-algorithm with the corresponding label.

**Naive-bayes** is a perfect algorithm for these kind of situation. It can naturally be adapted to multi-class problems, unlike many other algorithms in the list. Also, it performs in linear time, which is rare regarding other ML-algorithms. Also, the assumption that the features are independet turns out to give very good results. Basically it says that the class features are not dependent on each other. For example, some keywords for a database class may be the words SQL and database. Naive bayes will assume that these are not related but clearly they are.

**Maximum Entropy** is also a great candidate for multiclass classification problems. It has been showed in different tests that MaxEnt is great for text categorization, see https://web.stanford.edu/class/cs124/lec/Maximum_Entropy_Classifiers.pdf on slide 15. It performs similar to Naive-Bayes because they are quite similar. However, Naive-Bayes predicts the possibilites for both the incoming data and the output, whereas  MaxEnt only predicts the output, given the data. This can however leed to overfitting. Also, MaxEnt performs better when the amount of training data is large, which is good for this project where we have access to a large project.

**Support-Vector machines** is a binary classification algorithm that has shown great results in text classification problems. It works well and the performance of the algorithm is not dependent on the number of features that are avaible, but instead the margain between the features. It has also been noticed that SVM is perfect for high-dimensional data. This due to it "protection" against overfitting, which is common in other algorithms. Depending on the chosen feature-selection algorithm, SVMs performance can be improved both accuracy and timewise. Also acording to imperical studies, document vectors are often sparse, which is perfect for an algorithm like SVM. A intresting thing to test out is different kernel functions which stands for the linear transformation of the data. This has significant meaning for the overal performance of SVM.

**K-nearest neighbor **is a simple algorithm compared to the other listed. It does not "train" like the other algorithms, but instead, more data provides more search room. If the data is sparse and not easy to seperate, this algorithm will not work as good as intended, that is the data is not easy clustred. This algorithms efficency will depend mainly on the data-preprocessing. This algorithm also tends to use a lot of memory, which in our case may be inpracticle because of the large projects that are to be classified. An intresting thing to test if this algorithm is to be picked is to try out different types of K-values and see which K is best suited for our problem. 

**Decision trees** are intuitively easy to understand compared to the other algorithms in the list. It suffers from one major drawback, and it is the risk of overfitting. However, depending on the variant of decision trees that is used, some tackle this problem by using punning which "removes" branches in the tree which seems less important. Decision trees also has a hard time scaling with large amount of data, small changes in data can lead to the tree changing structure dramatically.  



## Sources
performance and info SVM: https://www.cs.cornell.edu/people/tj/publications/joachims_98a.pdf, https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/

Comparison between Naive-Bayes and MaxEnt : https://www.semanticscholar.org/paper/Comparison-between-Maximum-Entropy-and-Na%C3%AFve-Bayes-Maroulis/2c4638ff4eb16874a007b9f703453e2f6fdde24f

MaxEnt: https://web.stanford.edu/class/cs124/lec/Maximum_Entropy_Classifiers.pdf, https://blog.datumbox.com/machine-learning-tutorial-the-max-entropy-text-classifier/

General info: https://monkeylearn.com/blog/sentiment-analysis-machine-learning/

K-NN: https://www.kdnuggets.com/2017/09/rapidminer-k-nearest-neighbors-laziest-machine-learning-technique.html, http://ijcsit.com/docs/Volume%207/vol7issue1/ijcsit2016070156.pdf

Decision Trees: https://www.codementor.io/blog/text-classification-6mmol0q8oj












