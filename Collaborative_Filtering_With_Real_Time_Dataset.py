import pandas as pd

#These two datasets are from Movie Lens Dataset
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)

user_ratings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')

#Removing Movies which have less than ki 10 users who rated it & filling remaining NaN with 0
user_ratings = user_ratings.dropna(thresh=10,axis=1).fillna(0)

item_similarity_df = user_ratings.corr(method='pearson')

def get_similar_movies(movie_name,user_rating):
  similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
  similar_score = similar_score.sort_values(ascending=False)
  return similar_score

action_lover = [("2 Fast 2 Furious (Fast and the Furious 2, The) (2003)",5),("12 Years a Slave (2013)",4),("2012 (2009)",3),("(500) Days of Summer (2009)",2)]

similar_movies = pd.DataFrame();

for movie,rating in action_lover:
  similar_movies = similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)

print(similar_movies.sum().sort_values(ascending=False))
