# Cyber-Attack-Detection
Designed and implemented an Artificial Neural Network (ANN) model to predict cyber attack with 11 attack classes using Python, Keras/TensorFlow, and Sklearn with 98.01% accuracy.

Purpose:
The purpose of this experiment is to give us the data, so that we can carry out data screening (distinguish
between useful data and useless data), the data will be imported into a well-built python or matlab to
establish the ANN model, and ultimately, through the different proportion of the training and testing, to
determine the accuracy of the training results and very good to get the knowledge of the ANN aspects of
the training.

The study utilizes a dataset stored in 'cleaned_data_drop.csv', which is a preprocessed version of a larger
network traffic dataset. Initially, the dataset comprised 329,064 samples with 27 features, covering various
types of network activities including normal traffic and different categories of attacks.

This ANN model achieved 97% accuracy. Approximately 70% of the original dataset consisted of duplicate
values and the remaining 30% was reduced further to maintain class imbalance. Final model with highest
accuracy was trained on 12,063 rows.
Duplication and Class imbalance was a major limitation of this project since we had to reduce the dataset
by 99%. There were also computational constraints since the original dataset on KDD website was in .gz
format and was converted to .csv manually that required intensive computational power.
In future we plan on using the original data available on the KDD Cup website, for this project we will
harness the power of Matlab to analyze the data, perform exploratory data analytics and finally train the
ANN model.
