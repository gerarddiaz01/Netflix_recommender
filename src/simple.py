import pandas as pd
from recommender import load_and_prepare_data, build_similarity_matrix, get_recommendations

# Loads and preprocesses the Netflix dataset and returns a cleaned DataFrame ready for analysis
df = load_and_prepare_data()

# Builds a similarity matrix from the DataFrame, which quantifies how similar each title is to every other title
sim_matrix = build_similarity_matrix(df)

# Gets the input from the user and attempts to find the closes matching title and retrieves the top recommendations based on similarity
title = input("🎬 Enter a movie or TV show: ")
matched_title, recs = get_recommendations(title, df, sim_matrix)

# If no recommendations are found print an error message, otherwise display the matched title and recommendations
if isinstance(recs, list) and not recs:
    print(matched_title)  # error message
else:
    print(f"\n🔎 Top recommendations for: {matched_title}")
    for i, row in recs.iterrows():
        print(f"{row['Title']} ({row['Release Date']}) - {row['Genres']}")