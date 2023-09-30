# Horror Movies Exercise

Code Louisville Data Analysis Exercise

## Overview

In this exercise we will write a sql query against a database of movies. This 
exercise is based on the 
[Codecademy Learn SQL](https://www.codecademy.com/enrolled/courses/learn-sql) 
"Queries" module.

### `movies` Table
| column | type | constraint |
| ------ | ---- | ---------- |
| id | INTEGER | PRIMARY KEY |
| name | TEXT | NOT NULL |
| genre | TEXT | |
| year | INTEGER | |
| imdb_rating | REAL | |

Write a SQL query that returns the id, name and imdb rating of top 3 movies in 
the horror genre that were released in or before 1985. Note that the column 
names in the resulting file have been changed from "id", "name", and 
"imdb_rating" to "Movie_ID", "Movie_Title", and "Rating".

### Example Output Data

| Movie_ID | Movie_Title | Rating |
| -------- | ------ | ---- |
| 226 | The Shining | 8.4 |
| 100 | Gremlins | 7.2 |
| 116 | The Amityville Horror | 6.2 |

You will write your query in the `sql/horror_movies.sql` file. Running the 
`run_sql.py` script will execute your query and save the results to 
`data/movies.csv`.

## Instructions

1. Clone the repo to your machine.
1. Create a virtual environment and install the packages listed in the 
`requirements.txt` file (instructions below).
1. Add your SQL query to the `sql/horror_movies.sql` file.
1. Run the `run_sql.py` script. This script will execute your query against the 
database and save the results to `data/movies.csv`.
1. Add, Commit, and Push your `sql/horror_movies.sql` and `data/movies.csv` 
files back to GitHub.

###  Virutal Environment Instructions

1. After you have cloned the repo to your machine, navigate to the project 
folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
1. Activate the virtual environment. `source venv/bin/activate`
1. Install the required packages. `pip install -r requirements.txt`
1. When you are done working on your repo, deactivate the virtual environment. 
`deactivate`

[^1]: GitBash on Windows uses “python” instead of “python3”

### Automated Testing

This repo contains a small testing program that is automatically run by GitHub 
to validate your code. This testing program is contained in the tests.py file. 
You don't have to do anything with this file to complete the exercise, but you 
can follow these steps if you would like to run the tests on your machine.

1. Open GitBash in Windows or the Terminal in Mac and navigate to the project 
folder.
1. Activate the virtual environment if it is not already active.
1. Use the following command to run the tests: `pytest tests.py`. 
1. Review the output from running the test. This will let you know whether your 
code produces the expected results.
