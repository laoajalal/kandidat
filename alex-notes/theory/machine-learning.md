# Machine Learning
Machine Learning (ML) is a subfield of Artificial Intelligence, it's
explained by Arthur Samuel 
    " the field of study that gives computers the ability to learn without
    being explicitly programmed."
It builds a model based on sample data that usually is called "training data",
from that model it makes predictions or decisions without being explicitly 
programmed to do so.

ML uses mathematical optimization for its methods, theory and application.

Then what is the difference between ML and AI? *Judea Pearl* in *The Book of 
Why*, where it's noted that ML learns and predicts on passive observations
whereas AI have an agent that interacts with the environment to learn and take 
actions that maximize its chance of success.

#### What can ML do?
- Prediction, can be used to calculate probabilities and predictions
- Image recognition, e.g. face detection in images.
- Text recognition
- Speech recognition, whereas it translates the spoken words into text
- Medical diagnoses, can be trained to recognize cancerous tissues
- Finance, can be used in fraud investigations and credit checks

#### When do you need ML?
Usually human capabilities is limited in handling massive amounts of data and then 
extracting useful conclusions from said datasets this is where ML comes in,
e.g. transforming medical records into medical knowledge, forecasting weather, 
web-search engines.

#### ML history
1. Artificial Intelligence (AI)
2. Machine Learning (ML), a subset of AI  
   algorithm that allows software to become more accurate in its predictions 
   of its outcomes without being explicitly programmed.
3. Deep Learning (DL), a subset of ML

Started with a program in 1950s able to beat checkers players with the help of
ML, at the same time Frank Rosenblatt invented the Perceptron. It's a neural 
network that tries to mirrors the brain.

Thanks to statistics, it gave the probalistic approach to AI.

#### Types of learning
- [Supervised-Learning](supervised-learning-310121-2011.md):
- Unsupervised learning:
    - The AI systme is given a unlabeled data set, and its algorithms act on  
      the data without prior training.
    - Types:
        - Clusetering, look at the inherent groupings in the data.
        - Association, discovers rules that descripe large portions of the data.
- Reinforcement learning:
    - The AI system learns by interacting with its enviroment. It is a type of  
      dynamic programming that trains algorithms using a system of rewards  
      and penalties.

#### Approaches to learnings
- Feature learning, discovers features or representations through examinations,  
  without relying on explicit algorithms.
- Sparse dictionary learning, used in e.g. image de-noising.
- Anomaly detection or outlier detection. Identifies rare items, events or 
  observations that differs significantly from the majority of the data.
- Robot learning
- Association rule learning (inductive logic programming), rule-based method  
  for discovering relationships between variables i large databases.

#### Models
- Artificial Neural Network (ANN), often shows up in the topic of deep learning
- Decision tree, uses a tree model as a predictive model. The target variable  
  can take a discrete set of values that are called classification trees,
  the leaves represents class labels and the branches conjunctions of features 
  that lead to those labels.
- Support Vector Machines (SVMs), also known as Support Vector Networks.  
  Are a set of related supervised learning methods used for classification or  
  regression.
- Regression analysis
- Bayesian network, is a directed acyclic graphical model which is a
  probabilistic graphical model.
- Genetic algorithms
#### Training models
Federated learning
#### Model Assessment

#### Classifiers
- Bayesian:
    - Naive Bayes
    - Naive Bayes Multinomial
- Decision tree:
    - Decision stump
    - Hoeffding tree
    - Hoeffding option tree
    - Hoeffding adaptive tree
- Meta:
    - bagging
    - boosting
    - bagging using ADWIN
    - bagging using Adaptive-size hoeffding trees
    - perceptron stacking of restricted hoeffding trees
    - leveraging bagging
    - online accuracy updated ensemble
- Function:
    - perceptron
    - stochastic gradient descent (SGD)
    - pegasos
- Drift:
    - self-adjusting memory
    - probabilistic adaptvie windowing
- multi-label classifiers
- Active learning classifiers
