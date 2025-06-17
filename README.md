# Netflix Content-Based Recommender 🎬

This project is a real, working content-based recommendation system for Netflix movies and TV shows.You type in a movie or show you liked, and it suggests similar titles based on genres, director, cast, and description — all powered by TF-IDF vectorization and cosine similarity.

As a student learning Python and machine learning, I built this project to practice real-world data science skills. To help other learners, I’ve included an `Explanations.md` file that breaks down technical terms like vectorization and cosine similarity in simple language.

---

## Learning Context 📚

I built this in May 2025, during my fourth month learning Python. At this stage, I wanted to go beyond scripts and build a logic-first, data-driven application using real tools from the data science world.

This was my first time working with:
- A large external dataset.
- Data cleaning and vectorization.
- Scikit-learn’s similarity functions.
- A modular project split across multiple files.

I had to learn new concepts like TF-IDF, cosine similarity, and feature engineering while building. It wasn’t easy — but I documented my process, created a learner-focused Explanations.md, and wrote the app in a way others can follow.

This is what, I hope, will make me grow as a developer, getting out of my confort zone and thinking outside the box.

---

## Project Structure 📁

netflix_recommender/
├── data/
│   └── netflixData.csv
├── src/
│   ├── simple.py      # Terminal interface
│   ├── gui.py         # Graphical user interface (tkinter)
│   └── recommender.py # Core recommendation logic
├── requirements.txt
├── README.md
└── Explanations.md    # Technical terms explained for students

---

## Features ✨

- Input a movie or TV show title and get the top 5 most similar titles from the Netflix catalog.
- Fuzzy matching: handles typos and close matches.
- Optional filter: show only Movies, only TV Shows, or both.
- Two ways to use:
  - **Terminal script**: classic command-line interaction.
  - **GUI app**: user-friendly window built with tkinter.

---

## Technologies and Concepts Used 🧰

- Python 3
- pandas for data loading & manipulation
- scikit-learn: TfidfVectorizer, cosine_similarity
- difflib: Fuzzy matching for user input
- tkinter: GUI interface

---

## Dataset 📊

Netflix Movies and TV Shows from Kaggle  
https://www.kaggle.com/datasets/shivamb/netflix-shows

Place the file `netflixData.csv` inside the `data/` folder.

---

## Getting Started 🚀

1. Clone the repo

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add the dataset

Download `netflixData.csv` from Kaggle and place it in the `data/` folder.

---

## How the Recommendation Engine Works 🧠

The app is powered by a content-based filtering algorithm that lives in `recommender.py`. Here’s how it finds similar titles:

1. Preprocess data and Combine features: 
The script loads the Netflix dataset and combines important columns (director, cast, genres, description) into a single string for each title. All text is lowercased and cleaned to ensure consistency.

2. Vectorization (TF-IDF):
Each combined string is transformed into a vector of numbers using TF-IDF (Term Frequency-Inverse Document Frequency). This process highlights unique words that help define each title.

3. Compare: 
Use cosine similarity between every pair of titles to measure closeness between vectors in terms of their content features, regardless of their length.

4. Fuzzy Title Matching:
When a user enters a title, the system finds the closest match (even if there are typos) using fuzzy matching.

5. Recommendation Selection:
The engine retrieves the top N most similar titles (excluding the original) and returns them for display.

---

## How to Use 🛠️

### Simple Terminal Script 💻

Before running the scripts make sure you are in /data to use the csv file with the dataset.
Run the recommender in your terminal:

```bash
python src/simple.py
```

- Enter a movie or TV show title when prompted.
- See the top 5 similar recommendations printed in the terminal.

### GUI App 🪟

Run the graphical interface from the /data folder:

```bash
python src/gui.py
```

- Type or paste a title in the input box.
- Press Enter or click "Recommend".
- See the top 5 recommendations in the window.
- Use the filter to show only Movies, only TV Shows, or both.

---

## Challenges encountered and how I bypassed them 🧩

- Data inconsistencies
Some columns had missing values or inconsistent naming. I used fillna() and standard text cleaning functions.

- Fuzzy input
Typos like “Breaking Bad” → “Braking Bad” caused errors. The solution was to use difflib.get_close_matches() to smart-match input titles.

- Filtering by type
To let users filter between Movies / TV Shows, I added a column check and toggle in the GUI.

- Learning curve: Vectorization, TF-IDF and cosine similarity
At first, I didn’t understand these terms. I wrote everything I learned in Explanations.md, so future learners don’t feel lost like I did.

---

## For Students or beginners 👨‍🎓

Check out Explanations.md to learn:
- What is vectorization?
- How does cosine similarity work?
- Why not use spaCy, NLTK, or databases like SQLite here?
- Why tkinter over Streamlit for this use case?

These are explained in plain language — exactly how I taught myself.

---

## Conclusion 📝

This is the most technical project I’ve built so far — combining data science, text cleaning, vector math, and GUI design. It helped me grow as a developer by forcing me to learn real-world tools and make sense of abstract concepts.

I’m proud of how I handled:
- A large dataset
- Unknown libraries
- Confusing terms like “vector space”
- And still delivered something useful

There’s always room to improve it. But for now, it works — and I understand why it works.
This project reflects what I want to be known for: curious, clear, capable.

Thanks for reading.
