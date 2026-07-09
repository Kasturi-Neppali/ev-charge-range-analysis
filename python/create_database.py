
import pandas as pd
import sqlite3

# Create database connection
conn = sqlite3.connect("database/ev_database.db")

# -------------------------
# Dataset 1
# -------------------------
electric_car_data = pd.read_csv("dataset/ElectricCarData_Clean.csv")
electric_car_data.to_sql(
    "electric_car_data",
    conn,
    if_exists="replace",
    index=False
)

print("Table 'electric_car_data' created.")

# -------------------------
# Dataset 2
# -------------------------
ev_india = pd.read_csv("dataset/EVIndia.csv")
ev_india.to_sql(
    "ev_india",
    conn,
    if_exists="replace",
    index=False
)

print("Table 'ev_india' created.")

# -------------------------
# Dataset 3
# -------------------------
charging_stations = pd.read_csv(
    "dataset/electric_vehicle_charging_station_list.csv"
)

charging_stations.to_sql(
    "charging_stations",
    conn,
    if_exists="replace",
    index=False
)

print("Table 'charging_stations' created.")

# -------------------------
# Dataset 4
# -------------------------
cheapest_ev = pd.read_csv(
    "dataset/Cheapestelectriccars-EVDatabase.csv"
)

cheapest_ev.to_sql(
    "cheapest_ev",
    conn,
    if_exists="replace",
    index=False
)

print("Table 'cheapest_ev' created.")

conn.commit()
conn.close()

print("\nDatabase Created Successfully!")