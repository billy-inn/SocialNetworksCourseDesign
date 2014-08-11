# Usage

./run.sh 

PS: you should install python and octave or matlab in advance.

# Function

Given the input data file 'out.txt', split the data into training set and test set, use the logistic regression to predict the users' behavior.

We store the actual buying behaviors in the 'actual.txt' and the predicted buying behaviors in the 'predict.txt'.

Then we present the targets hit, the Precison, the Recall and eventually, the F1 value of our models.

# Format of the input data

The first column has a integer indicating the user Id;
The second column has a integer indicating the good Id;
The third column has a integer ranging from 0 to 3 indicating the type of user's behavior;
The fourth column has a integer indicating the date of the behavior.

# Format of the output data

Give two columns which indicate user Id and good Id.

