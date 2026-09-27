import pandas as pd

# Load results
df = pd.read_csv("data/soil_water_results.csv")

df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------------
# Define drought and recovery periods
# --------------------------------------------------

drought = df[
    (df["date"] >= "2023-06-01") &
    (df["date"] <= "2023-09-30")
]

recovery = df[
    (df["date"] >= "2023-10-01") &
    (df["date"] <= "2023-10-31")
]


# --------------------------------------------------
# Drought analysis
# --------------------------------------------------

scenarios = ["bare", "moderate", "high"]

print("\nDROUGHT PERIOD")
print("2023-06-01 to 2023-09-30\n")

for scenario in scenarios:

    storage = drought[f"{scenario}_storage_mm"]

    print(
        f"{scenario}: "
        f"start = {storage.iloc[0]:.2f} mm, "
        f"minimum = {storage.min():.2f} mm, "
        f"end = {storage.iloc[-1]:.2f} mm"
    )


# --------------------------------------------------
# Recovery analysis
# --------------------------------------------------

print("\nRECOVERY PERIOD")
print("2023-10-01 to 2023-10-31\n")

for scenario in scenarios:

    storage = recovery[f"{scenario}_storage_mm"]

    increase = storage.iloc[-1] - storage.iloc[0]

    print(
        f"{scenario}: "
        f"start = {storage.iloc[0]:.2f} mm, "
        f"end = {storage.iloc[-1]:.2f} mm, "
        f"increase = {increase:.2f} mm"
    )


# --------------------------------------------------
# Drainage during drought
# --------------------------------------------------

print("\nDROUGHT DRAINAGE\n")

for scenario in scenarios:

    drainage = drought[f"{scenario}_drainage_mm"].sum()

    print(
        f"{scenario}: "
        f"{drainage:.2f} mm"
    )