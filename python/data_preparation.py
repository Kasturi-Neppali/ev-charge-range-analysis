
import pandas as pd

# -----------------------------
# Load all datasets
# -----------------------------

electric_car_data = pd.read_csv("dataset/ElectricCarData_Clean.csv")
ev_india = pd.read_csv("dataset/EVIndia.csv")
charging_stations = pd.read_csv("dataset/electric_vehicle_charging_station_list.csv")
cheapest_ev = pd.read_csv("dataset/Cheapestelectriccars-EVDatabase.csv")


datasets = {
    "Electric Car Data": electric_car_data,
    "EV India": ev_india,
    "Charging Stations": charging_stations,
    "Cheapest EV": cheapest_ev
}


for name, df in datasets.items():

    print("\n" + "=" * 70)
    print(name)
    print("=" * 70)

    print("\nShape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)
    import pandas as pd

# ----------------------------
# Load datasets
# ----------------------------

electric_car_data = pd.read_csv("dataset/ElectricCarData_Clean.csv")
ev_india = pd.read_csv("dataset/EVIndia.csv")
charging_stations = pd.read_csv("dataset/electric_vehicle_charging_station_list.csv")
cheapest_ev = pd.read_csv("dataset/Cheapestelectriccars-EVDatabase.csv")

# ----------------------------
# Remove duplicate rows
# ----------------------------

charging_stations = charging_stations.drop_duplicates()

# ----------------------------
# Save cleaned datasets
# ----------------------------

electric_car_data.to_csv(
    "cleaned_data/ElectricCarData_Clean.csv",
    index=False
)

ev_india.to_csv(
    "cleaned_data/EVIndia.csv",
    index=False
)

charging_stations.to_csv(
    "cleaned_data/electric_vehicle_charging_station_list.csv",
    index=False
)

cheapest_ev.to_csv(
    "cleaned_data/Cheapestelectriccars-EVDatabase.csv",
    index=False
)

print("All cleaned datasets saved successfully!")

print("\nCharging Station Records After Cleaning:")
print(charging_stations.shape)