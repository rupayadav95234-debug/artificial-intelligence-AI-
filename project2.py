import pandas as pd

# Ek chota sa movies ka dataset (data) banate hain
movies_data = {
    'Movie_ID': [1, 2, 3, 4, 5, 6],
    'Title': ['The Dark Knight', 'Avengers: Endgame', 'The Hangover', 'Superbad', 'The Conjuring', 'Insidious'],
    'Genre': ['Action', 'Action', 'Comedy', 'Comedy', 'Horror', 'Horror']
}

df = pd.DataFrame(movies_data)

# Movie recommend karne ka function
def recommend_movies(user_favorite_genre):
    recommendations = df[df['Genre'].str.lower() == user_favorite_genre.lower()]
    return recommendations[['Title', 'Genre']]

# User se uski pasand poochhein
print("--- Movie Recommendation System ---")
user_choice = "Action"
print(f"Movies recommended for '{user_choice}' lovers:")

result = recommend_movies(user_choice)
print(result.to_string(index=False))
