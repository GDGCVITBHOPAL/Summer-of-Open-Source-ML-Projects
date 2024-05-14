import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

books= pd.read_csv("Books.csv")
users= pd.read_csv("Users.csv")
ratings= pd.read_csv("Ratings.csv")

#Merging dataset
ratings_with_name= ratings.merge(books, on='ISBN')
num_rating_df=ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'}, inplace=True)


avg_with_name= ratings.merge(books, on='ISBN')
avg_rating_df = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()

avg_rating_df.rename(columns={'Book-Rating':'avg_ratings'}, inplace=True)

popular_df= num_rating_df.merge(avg_rating_df, on='Book-Title')

popular_df[popular_df['num_ratings']>=250].sort_values('avg_ratings',ascending=False).head(50)

popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','avg_ratings','num_ratings']]

#Building the model
x= ratings_with_name.groupby('User-ID').count()['Book-Rating']>200
padhe_likhe_users= x[x].index

filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(padhe_likhe_users)]

y = filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50
famous_books = y[y].index
final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]

pt = final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')

pt.fillna(0,inplace=True)


similarity_scores = cosine_similarity(pt)



def recommend(book_name):
    print("Book name:", book_name)

    # index fetch
    index = pt.index.get_loc(book_name)
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:5]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        
        
       

        data.append(item)
    

    return data
recommendations = recommend('1984')
print("Recommendations:", recommendations)


books.drop_duplicates('Book-Title')