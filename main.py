import mysql.connector
import os
import pandas as pd
import matplotlib.pyplot as plt


# 1. Database Connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="transitpulse",
    connection_timeout=5,
    use_pure=True
)

print("MySQL Connected Successfully!")
cursor = connection.cursor()

# 2. Fetching all bus journeys
cursor.execute("SELECT * FROM bus_journeys")
for row in cursor.fetchall():
    print(row)

# 3. Route Analysis using Pandas & Matplotlib
query = """
SELECT route_name, AVG(travel_time) AS average_time
FROM bus_journeys
GROUP BY route_name
"""

df_routes = pd.read_sql(query, connection)

print("\nRoute Analysis:")
print(df_routes)

plt.bar(df_routes["route_name"], df_routes["average_time"])
plt.title("Average Travel Time by Route")
plt.xlabel("Bus Route")
plt.ylabel("Average Travel Time (minutes)")
plt.show()

connection.close()


# 4. CSV File Analysis (Segment Data)
print("\n--- Segment Level Data Analysis ---")

df_csv = pd.read_csv("data/segment_level_data.csv")

print("First 5 Rows:")
print(df_csv.head())

print("\nColumn Names:")
print(df_csv.columns.tolist())

print("\nDataset Shape:")
print(df_csv.shape)

# Loading sample rows for quick analysis
df_sample = pd.read_csv("data/segment_level_data.csv", nrows=10000)

print("\nRows loaded:", len(df_sample))
print("Average travel time (seconds):", df_sample["run_time_in_seconds"].mean())

# Segment-wise breakdown
segment_analysis = df_sample.groupby("segment")["run_time_in_seconds"].mean()
print("\nSegment-wise Averages:")
print(segment_analysis.head(10))

# Plotting top segments
top_segments = segment_analysis.head(10)
top_segments.plot(kind="bar")

plt.title("Average Travel Time by Segment")
plt.xlabel("Segment Number")
plt.ylabel("Average Travel Time (Seconds)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()