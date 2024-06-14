A model on classifying Survived, based on the kaggle dataset Titanic.

We used RandomForestClassifier to achieve an accuracy of 80.6%, with an AUC of 78.7%.

<!-- By Ritik Tiwari -->
Key Improvements:

1.Handled missing values in 'Embarked' before encoding.
2.Used inplace=True for dropping columns.
3.Filled missing values directly using pandas methods.
4.Split data before scaling to prevent data leakage.
5.Used fitted scaler on the training set to transform the test set.

Result: improved Accuracy: 81.7%
        and AUC-ROC Score: 79.77%