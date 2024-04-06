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

Contributing

Contributors are welcome to improve the analysis or extend the dataset. Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Thanks to those who have contributed to the dataset and to the development of tools that made this analysis possible.

Contact

For any queries or further discussion, please contact the repository owner.
