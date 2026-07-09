
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database/ev_database.db")

# -------------------------------
# Business Question 1
# -------------------------------

query = """
SELECT COUNT(*) AS Total_Cars
FROM electric_car_data;
"""

result = pd.read_sql(query, conn)

print("Business Question 1")
print("How many electric cars are available?\n")

print(result)

conn.close()







import sqlite3
import pandas as pd

# Connect to SQLite Database
conn = sqlite3.connect("database/ev_database.db")

# Function to execute SQL query
def execute_query(title, query):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    result = pd.read_sql(query, conn)
    print(result)


# ----------------------------
# QUERY 1
# ----------------------------

execute_query(
    "1. Total Number of Electric Cars",
    """
    SELECT COUNT(*) AS Total_Cars
    FROM electric_car_data;
    """
)

# ----------------------------
# QUERY 2
# ----------------------------

execute_query(
    "2. Top 10 Most Expensive Cars",
    """
    SELECT Brand, Model, PriceEuro
    FROM electric_car_data
    ORDER BY PriceEuro DESC
    LIMIT 10;
    """
)

# ----------------------------
# QUERY 3
# ----------------------------

execute_query(
    "3. Top 10 Highest Range Cars",
    """
    SELECT Brand, Model, Range_Km
    FROM electric_car_data
    ORDER BY Range_Km DESC
    LIMIT 10;
    """
)

# ----------------------------
# QUERY 4
# ----------------------------

execute_query(
    "4. Number of Cars by Brand",
    """
    SELECT Brand,
           COUNT(*) AS Total_Cars
    FROM electric_car_data
    GROUP BY Brand
    ORDER BY Total_Cars DESC;
    """
)

# ----------------------------
# QUERY 5
# ----------------------------

execute_query(
    "5. Average Price",
    """
    SELECT AVG(PriceEuro) AS Average_Price
    FROM electric_car_data;
    """
)

# ----------------------------
# QUERY 6
# ----------------------------

execute_query(
    "6. Average Electric Range",
    """
    SELECT AVG(Range_Km) AS Average_Range
    FROM electric_car_data;
    """
)

# ----------------------------
# QUERY 7
# ----------------------------

execute_query(
    "7. Body Style Distribution",
    """
    SELECT BodyStyle,
           COUNT(*) AS Total
    FROM electric_car_data
    GROUP BY BodyStyle;
    """
)

# ----------------------------
# QUERY 8
# ----------------------------

execute_query(
    "8. Power Train Distribution",
    """
    SELECT PowerTrain,
           COUNT(*) AS Total
    FROM electric_car_data
    GROUP BY PowerTrain;
    """
)

# ----------------------------
# QUERY 9
# ----------------------------

execute_query(
    "9. Rapid Charging Support",
    """
    SELECT RapidCharge,
           COUNT(*) AS Total
    FROM electric_car_data
    GROUP BY RapidCharge;
    """
)

# ----------------------------
# QUERY 10
# ----------------------------

execute_query(
    "10. Cars Having More Than 500 KM Range",
    """
    SELECT Brand,
           Model,
           Range_Km
    FROM electric_car_data
    WHERE Range_Km > 500;
    """
)

# Close database
conn.close()

print("\nAll SQL Queries Executed Successfully!")