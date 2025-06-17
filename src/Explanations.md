- Vectorizing text + similarity:
Why I am using scikit-learn?
TfidfVectorizer:	Turns movie info (cast, genre, etc.) into numerical vectors automatically
cosine_similarity:	Efficiently computes how similar two movies are
Easy to learn:	No math from scratch — just plug and play
Built for content-based recommendations:	Ideal for my "based-on-textual-content" goal
Fast:	Handles thousands of titles with ease

- UI:
Why I am using tkinter?
Built-in GUI toolkit in Python:	   No installation needed
Lightweight:	Perfect for basic input/output GUIs
Easy layout:	Just a window, entry box, button, and result list
Works well with small apps:    I don't need HTML/CSS/JavaScript like in web apps

Alternative like Streamlit is awesome for dashboards, but it:
Runs in a browser.
Needs a different way to structure the app (single-page layout).
Requires an always-running server.

Since my project is logic-first and beginner-friendly, tkinter is simpler and more than enough.

- Why I am not using NLTK/ spaCy for the advances NLP libraries?
NLTK is mostly used for processing natural language, it's not really needed for names and tags like "Keanu Reeves" 
and "Action, Thriller".
spaCy is even more advanced, it's good for sentence parsing, not for this kind of sahallow metadata.
Our input is already structured: Cast, genre, director don't need grammatical parsing.
Adds complexity: There's an extra learning curve and minimal benefit for this project, I am focusing on learning the basics 
for now, trying to achieve my goal and the straightest line is the easier one.

- Why Pandas and not SQLite?
Pandas can easily hold our entire CSV dataset, SQLite is only needed for huge datasets or multi-user apps, it's an overkill.
There's no need for real-time updates, we're not writing or storing user preferences.
Pandas is faster for analysis, there's no need for SQL querying here.

- Definitions:
1. Preprocess features:
This means cleaning and preparing your data so the computer can understand it.
Example: Making all text lowercase, removing weird symbols, and filling in missing info.

2. Vectorize:
Imagine turning words into numbers so a computer can do math with them.
Example: “action sci-fi” becomes a list of numbers, like [0.2, 0.8, 0, ...], so we can compare movies.

3. Cosine similarity:
This is a way to measure how similar two things are, using their “number lists” (vectors).
If two movies have similar words, their vectors “point” in the same direction, and cosine similarity will be close to 1 (very similar).
If they’re very different, it’s close to 0.

4. What is TF-IDF?
TF (Term Frequency): Counts how many times each word appears in the movie’s description.
IDF (Inverse Document Frequency): If a word is very common (like “movie”), it’s not special, so it gets less importance. Rare words (like “keanureeves”) are more special and get more importance.
TF-IDF: Combines these ideas so each movie is described by numbers that show which words are important for that movie.
