# Twitter Sentiment Analysis

This project aims to perform sentiment analysis on Twitter data using machine learning techniques. The sentiment analysis task involves predicting the sentiment (positive, negative, or neutral) of tweets.

## Prerequisites

Before running the code, make sure you have Python installed on your system along with the necessary libraries. You can install the required libraries using pip:

pip install -r requirements.txt

## Getting Started

1. Clone this repository to your local machine:

git clone https://github.com/your_username/twitter-sentiment-analysis.git

2. Navigate to the project directory:

cd twitter-sentiment-analysis

3. Place your Twitter data files (`twitter_training.csv` and `twitter_validation.csv`) in the project directory.

4. Run the Python script `sentiment_analysis.py`:
python sentiment_analysis.py


## Description

- `sentiment_analysis.py`: This script contains the code for preprocessing the data, training a logistic regression model, and evaluating the model's performance.

- `twitter_training.csv`: This CSV file contains the training data for the sentiment analysis task. It should have columns for tweet IDs, additional information (if any), tweet type, and tweet text.

- `twitter_validation.csv`: This CSV file contains the validation data for testing the trained model.

## Results

The accuracy of the trained model on the validation dataset is 83.65803039432282

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.




