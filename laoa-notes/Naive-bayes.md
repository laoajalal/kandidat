# Naive Bayes
Naive-Bayes algorithm is based on Bayes theorem P(A|B) = P(A) * P(B|A) / P(B).
- It assumes that the presence of a feature in a class is unrelated to the presence of any other feature.
- It is easy to build and useful for large datasets
- Known for outperforming more sophisticated classification methods.

## Pros
- It performs in linear time, thus its very fast for being a ML algorithm
- When the assumption that all features are independent, it perfroms very well
- Performs good in cases of categorical input variables

## Cons
- If a category has a label which has not yet been observed when the classifier was trainded, the model will assign the probability of 0 to it. TO solve this, different methods exists, called smoothing techniques. Also having diversity on the training data will solve this problem