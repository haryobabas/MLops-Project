# MLops-Project

Simple project to implement class in MLops for developing model SPAM detection using Naive Baiyes methods deploy in Google Cloud Run, the main objective of this project is to train VCS, Docker & CICD.

# Preparing Data

we use Dataset SPAM & HAM which have 5572 records of email that have proportion 747 Label SPAM email & 4825 Label HAM email. We labeled 0 for email HAM & 1 for SPAM email.

# Feature engineering

Because we used text data, for the feature engineering we decide to use Count Vectorizer. Count Vectorizer is a feature extraction technique that converts text data into a matrix representation based on word frequencies. It enables machine learning algorithms to process and analyze text data.

# Modeling & Evaluation

## Modeling

In this project we use Naive Bayes library from sklearn, especially MultiNomialNB. we seperate the data from train test with test set 0.2. we fit the data with the model.

## Evaluation

we use classification report include (Precision, Recall, F1-Score) to evaluation this model, and we get score :

                    precision           recall          f1-score        support

    0               0.99                0.98            0.99               991
    1               0.87                0.93            0.90               124

    accuracy                           0.98      1115

    macro avg       0.93                0.96           0.94                1115
    weighted avg    0.98                0.98           0.98                1115

After training and evaluating our model, we achieved an accuracy of 98% on the test set. The precision and recall values for spam detection were 0.87 and 0.93, respectively. These results indicate that our model effectively identifies spam emails while minimizing false positives.

# Format Message for Predict via API

Format message that API could read is JSON format, in detail like this :
'''json
{
"text": "(Value of message)"
}
'''
the user of API could input the text email that want to predict in (value of message), example like this:

'''json
{
"text": "(This is a promotion email to get discount)"
}
'''

# Format Response from API

currently for response API could divide by 3:

1. Status Code 200, {"prediction": "Ham"}
2. Status Code 200, {"prediction": "Spam"}
3. Status Code 400, {"detail": "Empty input text"}

# Conclusion and Future Work

In this project, we successfully developed a machine learning model for spam detection. However, there is still room for improvement. In the future, we plan to explore more advanced techniques such as deep learning models and ensemble methods to further enhance the accuracy and robustness of our spam detection system.
