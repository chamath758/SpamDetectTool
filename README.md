# SpamDetectTool
The SpamDetectTool repository is an advanced spam detecting tool using machine learning to filter out unwanted content from various sources.
# Methodology 
Data Collection

The first stage in creating a spam email detection technology is to gather a broad and representative dataset of spam and non-spam emails. This dataset will be used to train and evaluate the logistic regression model. To achieve this, we collect data various sources like Kaggle and we specially use custom dataset for train logistic regression model. 
 
•	The code begins by importing the required libraries, which include numpy, pandas, and scikit-learn.
•	It takes email data from a CSV file ('mail_data.csv') and stores it in a pandas DataFrame named 'raw_mail_data'.
•	Using the 'where' function, the null values in the DataFrame are replaced with a null string.
•	The 'head' method prints the top 5 rows of the preprocessed DataFrame.
•	The'shape' feature displays the DataFrame's size (number of rows and columns).
Custom Dataset 
 	
Labeling the Dataset 
 
•	The code labels the email categories as follows:'spam' is labeled as 0, and 'ham' (non-spam) is labeled as 1.
•	Variable 'X' is allocated to the email messages ('Message' column), and variable 'Y' is assigned to the relevant labels ('Category' column).
•	The code uses scikit-learn's 'train_test_split' function to divide the data into training and test sets, with 80% of the data utilized for training and 20% for testing.
Feature Extraction
The extraction of features is critical in training the logistic regression model. To extract meaningful information from an email dataset, both content-based and header-based features can be employed.
 
•	The function transforms the text input into feature vectors using scikit-learn's 'TfidfVectorizer'.
•	The 'TfidfVectorizer' translates text to a TF-IDF feature matrix, taking into account settings such as minimum document frequency, stop words, and lowercase conversion.
•	Using the 'fit_transform' and 'transform' functions, the training and test data are turned into feature vectors.

Model Training and Evaluation

 
 
•	The 'LogisticRegression' class from scikit-learn is used to create a logistic regression model.
•	The logistic regression model is trained using the training data's feature vectors.
•	Predictions are created using both training and test data, and the model's accuracy is calculated using the 'accuracy_score' function.
•	Both the training and test data accuracy is printed.




Prediction on New Data:
 
•	As 'input_mail,' an example email message is supplied, and feature extraction is used to transform it into a feature vector.
•	The logistic regression model predicts whether or not the input email is spam.
•	If the prediction is 1 (non-spam), the result is printed as 'Ham mail'; otherwise, it is printed as 'Spam mail'.

Model and Feature Extraction Saving:
 

•	Using the 'pickle' module, the trained logistic regression model is stored in a file named'model.pkl'.
•	Using the 'pickle' module, the feature extraction parameters are saved in a file called 'feature_extraction.pkl'.
Integration part
Using this python developed simple application for more user-friendly propose.
Code App.py 
   
 
