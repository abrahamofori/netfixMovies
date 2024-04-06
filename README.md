Netflix Movies Duration Analysis

Description

This project investigates the trend in movie durations on Netflix over time. Using a dataset named netflix_data.csv, we perform exploratory data analysis to determine if movies are indeed getting shorter. 
The analysis focuses on filtering the dataset to movie entries, examining their duration, and visualizing trends across different genres over the years.

Installation

No installation is needed. However, you should have Python installed, along with libraries like pandas and matplotlib to run the analysis script.

Usage

The script performs the following steps:

Load Data: Reads the netflix_data.csv file into a DataFrame named netflix_df.

Filter Data: Removes TV shows to focus solely on movies, storing the result in netflix_subset.

Data Preparation: Selects relevant columns ("title", "country", "genre", "release_year", "duration") and stores them in netflix_movies.

Analyze Short Movies: Filters netflix_movies to find movies shorter than 60 minutes, stored in short_movies and investigates potential contributing factors.

Visualization: Iterates through netflix_movies, assigning colors to genres and creating a scatter plot of movie duration against release year.

The analysis concludes with a discussion on the trend of movie durations over time.


Findings

The analysis involved loading the Netflix dataset, filtering to focus on movies, and examining the duration of these films over time, categorized by genre. We carefully analyzed the trends after creating a scatter plot to visualize the relationship between movie duration and release year.

The plots and analysis indicated that we cannot conclusively say movies' durations are declining. The evidence suggests that movie length varies significantly across different genres and periods, and a straightforward downward trend in movie duration is not evident. Therefore, we conclude that the claim of movies getting shorter over time needs more in-depth analysis to be substantiated.

Ongoing Work

I am currently working on a more detailed analysis to further investigate these trends. This involves examining additional factors that may affect movie duration and utilizing more advanced statistical techniques to analyze the data. The goal is to gain a clearer understanding of how and why movie durations may be changing over time.



Contributing

Contributors are welcome to improve the analysis or extend the dataset. Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.


Acknowledgments

Thanks to those who have contributed to the dataset and to the development of tools that made this analysis possible.

Special thanks to DataCamp for providing the educational resources and data that facilitated this analysis.

Contact

For any queries or further discussion, please contact the repository owner.
