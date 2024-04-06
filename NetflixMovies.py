# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:44:26 2024

@author: Abraham
"""

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df)
print(netflix_df.iloc[[1,2,3,4,5]])
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
print(netflix_subset)
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies)
short_movies = netflix_movies[netflix_movies["duration"]<60]
print(short_movies)
#For Loop to set colors to specified genres
colors = []
for row, column in netflix_movies.iterrows():
    if column['genre'] == "Children":
        color = "red"
    elif column['genre'] == "Documentaries":
        color = "yellow"
    elif column['genre'] == " Stand-Up":
        color = "green"
    else:
        color = "black"
    colors.append(color)
print(colors)
#Initializing Figure With specified With and Height
fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c = colors)
plt.xlabel("Release Year", fontsize=14)
plt.ylabel("Duration(min)", fontsize=14)
plt.title("Movie Duration by Year of Release", fontsize=14)
plt.show()

answer = "No, We need to do more Analysis on The Data"

print(answer)