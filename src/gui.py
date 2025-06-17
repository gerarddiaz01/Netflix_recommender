import tkinter as tk
from tkinter import messagebox
from recommender import load_and_prepare_data, build_similarity_matrix, get_recommendations

def recommend():
    '''Logic for generating and displaying recommendations in the GUI'''
    # Retrieves the user input text and removes any leading or trailing whitespace
    user_input = title_entry.get().strip()

    # Handle error (empty entry)
    if not user_input:
        messagebox.showwarning("Input error", "Please enter a title.")
        return

    # Get the closest title and recommendations
    matched_title, recs = get_recommendations(user_input, df, sim_matrix)

    output_text.delete("1.0", tk.END)  # Clear previous results

    # Handle error (no recommendation found) to avoid making the app crash
    if isinstance(recs, list) and not recs:
        output_text.insert(tk.END, matched_title)  # This is the error message
    else: # Applies the filter and gives the results
        filter_type = filter_var.get()
        if filter_type != "All":
            # Your DataFrame may use 'Content Type' or similar; adjust as needed
            recs = recs[recs['Content Type'] == filter_type]
        output_text.insert(tk.END, f"Top recommendations for: {matched_title.title()}\n\n")
        for i, row in recs.iterrows():
            line = f"{row['Title']} ({row['Release Date']}) - {row['Genres']}\n"
            output_text.insert(tk.END, line)

def on_typing(event):
    '''Set up a fresh area clearing previous results when the user starts typing'''
    output_text.delete("1.0", tk.END)

# Load data and similarity matrix once at startup
df = load_and_prepare_data()
sim_matrix = build_similarity_matrix(df)

# Initialize the GUI window
root = tk.Tk()
root.title("Netflix Recommender")
root.geometry("600x400")

# Set up the filter by type of recommendations
filter_var = tk.StringVar(value="All")

filter_frame = tk.Frame(root)
filter_frame.pack(pady=5)

tk.Label(filter_frame, text="Filter by type:").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(filter_frame, text="All", variable=filter_var, value="All").pack(side=tk.LEFT)
tk.Radiobutton(filter_frame, text="Movie", variable=filter_var, value="Movie").pack(side=tk.LEFT)
tk.Radiobutton(filter_frame, text="TV Show", variable=filter_var, value="TV Show").pack(side=tk.LEFT)

# Entry label
title_label = tk.Label(root, text="Enter a movie or show title:", font=("Arial", 12))
title_label.pack(pady=10)

# Input field
title_entry = tk.Entry(root, width=50, font=("Arial", 12))
title_entry.pack()

# Set up the cursor in the input box when the app starts, right away
title_entry.focus()

# Clear results when the user starts typing
title_entry.bind("<Key>", on_typing)

# Output area label
output_label = tk.Label(root, text="Recommendations:", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

# Output text area
output_text = tk.Text(root, height=10, width=70, wrap="word", font=("Arial", 11))
output_text.pack()

# Recommend button
recommend_button = tk.Button(root, text="Recommend", command=recommend, font=("Arial", 12))
recommend_button.pack(pady=10)

# Press enter to get recommendations, just like a search box
root.bind("<Return>", lambda event: recommend())

# Start the GUI loop
root.mainloop()