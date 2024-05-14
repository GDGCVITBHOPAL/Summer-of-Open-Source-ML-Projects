# Book Recommendation System

This project implements a book recommendation system based on user ratings data. The system utilizes collaborative filtering techniques to recommend books to users based on their preferences and behavior.

## Dataset

The dataset consists of three CSV files:

- `Books.csv`: Contains information about books including ISBN, title, author, and image URL.
- `Users.csv`: Contains information about users including user ID and demographic details.
- `Ratings.csv`: Contains user ratings for books, including the book's ISBN, user ID, and rating.

## Implementation

1. **Data Preprocessing**: The data is loaded into Pandas DataFrames and merged to create a unified dataset. The number of ratings and average ratings for each book are calculated.

2. **Filtering**: Users who have rated more than 200 books and books with at least 50 ratings are selected to build the recommendation model. 

3. **Pivot Table**: A pivot table is created where each row represents a book and each column represents a user, with ratings as the values. 

4. **Cosine Similarity**: Cosine similarity is computed between books based on user ratings, resulting in a similarity matrix.

5. **Recommendation Function**: A function is implemented to recommend similar books to a given book. It takes the book title as input and returns a list of recommended books based on similarity scores.

6. **Example Usage**: An example recommendation is provided, recommending books similar to "1984".

## Usage

1. Clone this repository to your local machine:
git clone https://github.com/your_username/book-recommendation-system.git

2. Navigate to the project directory:

3. Place your dataset files (`Books.csv`, `Users.csv`, `Ratings.csv`) in the project directory.

4. Run the Python script `recommendation_system.py`:
python recommendation_system.py


5. Use the `recommend()` function to get recommendations for a specific book:

```python
recommendations = recommend('1984')
print("Recommendations:", recommendations)

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

