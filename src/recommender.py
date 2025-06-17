import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

def load_and_prepare_data(csv_path="data/netflixData.csv"):
    '''Function to load and preprocess my Netflix data'''
    # Load the csv file into a pandas DateFrame
    df = pd.read_csv(csv_path)

    # Fill missing values with empty strings to act as placeholders, for data consistency and avoid future errors when we do text vectorization
    for col in ['Director', 'Cast', 'Genres', 'Description']:
        df[col] = df[col].fillna("")

    # Helper function to clean text: lowercase, remove punctuation, remove spaces
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
        text = text.replace(" ", "")         # remove spaces
        return text
    # Apply the cleaning function to each value of the specified columns
    df['Director'] = df['Director'].apply(clean_text)
    df['Cast'] = df['Cast'].apply(clean_text)
    df['Genres'] = df['Genres'].apply(clean_text)
    df['Description'] = df['Description'].apply(clean_text)

    # New column to combine all features into one string already cleaned and ready to be used
    df['combined_features'] = (
        df['Director'] + " " +
        df['Cast'] + " " +
        df['Genres'] + " " +
        df['Description']
    )
    # Returns the processed DataFrame to use elsewhere in my project
    return df

def build_similarity_matrix(df):
    '''Function to create a similarity matrix from the DataFrame'''
    # Create a TF-IDF vectorizer that ignores common English words (turn data into numbers)
    vectorizer = TfidfVectorizer(stop_words='english')
    # Convert the combined text into a matrix of numbers (vectors)
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

    # Compute cosine similarity
    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix

def get_recommendations(title, df, sim_matrix, top_n=5):
    '''Takes a movie or TV show, finds it in the DataFrame, and returns the top N most similar titles based on the similarity matrix'''
    # Clean the user input by making it lowercase and removing extra spaces
    title = title.lower().strip()

    # Creates a mapping from lowercase title names to their row index in the DataFrame, to find exact or close matches
    title_map = {t.lower(): i for i, t in enumerate(df['Title'])}
    all_titles = list(title_map.keys())

    # If there's no exact match, it uses fuzzy matching to find the closest data, if no match found return error
    if title not in title_map:
        matches = get_close_matches(title, all_titles, n=1, cutoff=0.6)
        if not matches:
            return f"❌ Title '{title}' not found. Try another.", []
        title = matches[0]

    # Finds the index of the matched title in the DataFrame, and using the similarity matrix get the similarity scores
    idx = title_map[title]
    similarity_scores = list(enumerate(sim_matrix[idx]))

    # Sort by similarity score, exclude the same movie (index == idx)
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i for i, score in sorted_scores if i != idx][:top_n]

    # Retrieves the recommended rows from the DataFrame, showing only the most relevant columns
    recommendations = df.iloc[top_indices][['Title', 'Director', 'Genres', 'Release Date', 'Content Type']]
    return title, recommendations