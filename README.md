EU countries Economic Data Explorer
Overview
This web application allows users to explore economic data for different EU cities, utilizing data from "global_economy.csv" and "eu_countries.csv" as open-source databases.

Design
The application's design includes two main pages: "index.html" for displaying cities and "show.html" for showing detailed economic data of the selected city.

Development
The application is developed using the Flask framework and SQLite database. It includes scripts like "parse_csv.py" for processing CSV data and "economic_data.py" for handling Flask routes and database interactions.

Flask Application Setup code
![image](https://github.com/XuanYu0721/CA3/assets/161028690/5d4c020c-626f-4ce4-9cb2-0470039aec66)

Implementation
The Flask framework manages the application's server-side logic, while SQLite is used for data storage and retrieval. The application efficiently processes and displays economic data from CSV files.

Database Interaction code
![image](https://github.com/XuanYu0721/CA3/assets/161028690/8c3b9030-582f-432c-aa71-2c2d52dfa1a7)

Usage
Navigate through the "index.html" page to view a list of cities and click on a city to view its economic data on the "show.html" page.

Contributing
Feel free to contribute by forking the repository, making improvements, and submitting pull requests.

Render deployment URL： https://ca3-j6ih.onrender.com
