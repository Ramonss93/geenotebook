### What is Machine Learning?
Machine learning is the process to automatically extract knowledge from data, usually with the goal of making predictions on new, unseen data.

Central to machine learning is the concept of **making decision automatically** from data, **without the user specifying explicit rules** how this decision should be made.

### generalization
The goal of a machine learning algorithm is to predict on new, previously unseen data. We are not interested in marking an email as spam or not, that the human already labeled. Instead, we want to make the users life easier by making an automatic decision for new incoming mail.

### Supervised Learning: Classification and regression
construct a model (or program) which is able to predict the desired output of an unseen object given the set of features.

Supervised learning is further broken down into two categories, classification and regression.

In supervised learning, there is always a distinction between a training set for which the desired outcome is given, and a test set for which the desired outcome needs to be inferred.

### Unsupervised Learning
no desired output associated with the data. Instead, we are interested in extracting some form of knowledge or model from the given data. In a sense, you can think of unsupervised learning as a means of discovering labels from the data itself. Unsupervised learning is often harder to understand and to evaluate.

Unsupervised learning comprises tasks such as __dimensionality reduction__, __clustering__, and __density estimation__.

Sometimes the two may even be combined: e.g. Unsupervised learning can be used to find useful features in heterogeneous data, and then these features can be used within a supervised framework.

### Data in scikit-learn
data stored as a two-dimensional array

- n_samples: The number of samples: each sample is an item to process (e.g. classify). A sample can be a document, a picture, a sound, a video, an astronomical object, a row in database or CSV file, or whatever you can describe with a fixed set of quantitative traits.
- n_features: The number of features or distinct traits that can be used to describe each item in a quantitative manner. Features are generally real-valued, but may be boolean or discrete-valued in some cases.

### Training and Testing Data
Now we need to split the data into training and testing. Luckily, this is a common pattern in machine learning and scikit-learn has a prebuilt function to split data into training and testing for you. Here we use 50% of the data as training, and 50% testing. 80% and 20% is another common split, but there are no hard and fast rules. The most important thing is to fairly evaluate your system on data it has not seen during training!

```
from sklearn.cross_validation import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, random_state=1999)
print("Labels for training and testing data")
print(train_y)
print(test_y)
```
