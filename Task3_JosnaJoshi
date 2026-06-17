movie_recommendations = {
    "Action": ["John Wick", "Avengers", "Bad Boys"],
    "Comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "Horror": ["The Conjuring", "From", "Annabelle"],
    "Romance": ["Titanic", "The Notebook", "La La Land"]
}

print("Welcome to the Movie Recommendation System!")

favorite_genre = input("Enter your favorite genre (Action, Comedy, Horror, Romance): ")

if favorite_genre in movie_recommendations:
    print("\nBased on your interest, we recommend:")
    
    for movie in movie_recommendations[favorite_genre]:
        print(f"• {movie}")
else:
    print("\nSorry! No recommendations found for that genre.")
