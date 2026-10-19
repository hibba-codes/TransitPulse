# TransitPulse 🚌

A beginner-friendly data analytics project that explores bus journey and road segment travel times using Python, MySQL, Pandas, and Matplotlib.

## 📌 About the Project

TransitPulse is a mini data analytics project developed to practice working with transportation data. It analyzes average travel times across bus routes and road segments and presents the results using charts.

## 🎯 Project Objectives

- Retrieve bus journey data from a MySQL database.
- Calculate average travel time for each bus route.
- Explore a CSV dataset using Pandas.
- Calculate average travel time by road segment.
- Visualize travel-time analysis using bar charts.

## 🛠️ Technologies Used

- Python
- MySQL
- Pandas
- Matplotlib

## 📊 Project Features

### 1. MySQL Database Analysis

- Connects Python to a MySQL database.
- Retrieves bus journey records from the `bus_journeys` table.
- Calculates average travel time for each route using SQL.

### 2. Route-Wise Visualization

- Displays average travel time for each bus route.
- Creates a bar chart to compare route travel times.

### 3. CSV Dataset Analysis

- Reads segment-level data from a CSV file.
- Displays the first five rows, column names, and dataset dimensions.
- Loads a sample of 10,000 rows for analysis.
- Calculates average travel time by road segment.
- Creates a bar chart showing the first ten segment averages.

## 📁 Project Structure

    TransitPulse/
    ├── data/
    │   └── segment_level_data.csv
    ├── main.py
    └── README.md

**Note:** The CSV dataset is not included in this repository because of its large file size. The dataset must be available locally to run the segment analysis.

## ⚙️ Requirements

- Python
- MySQL Server
- A MySQL database named `transitpulse`
- A `bus_journeys` table with the required columns
- The segment-level CSV dataset

## 📦 Python Libraries

Install the required libraries using:

    pip install mysql-connector-python pandas matplotlib

## ▶️ How to Run

1. Download or clone this repository.
2. Set up the MySQL database and the required `bus_journeys` table.
3. Place the CSV dataset inside the `data` folder.
4. Set the `MYSQL_PASSWORD` environment variable to your MySQL password.
5. Run the Python script:

    python main.py

## 📚 Learning Outcomes

Through this project, I practiced:

- Connecting Python with MySQL.
- Writing SQL queries using `SELECT`, `AVG()`, and `GROUP BY`.
- Reading CSV files with Pandas.
- Exploring and grouping data.
- Calculating average values.
- Creating bar charts with Matplotlib.

## 👩‍💻 Author

**Hibba Iqbal**

Aspiring Data Analyst | Data Science Student
