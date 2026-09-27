import pandas as pd
import numpy as np
from pathlib import Path

# --------------------------------------------------
# 1. Load climate data
# --------------------------------------------------

data_path = Path("data/synthetic_climate.csv")
df = pd.read_csv(data_path)

rainfall = df["rainfall_mm"].values
temperature = df["temperature_C"].values


# --------------------------------------------------
# 2. Soil-water balance model
# --------------------------------------------------

def run_model(rainfall, temperature, vegetation_factor):

    # Initial soil-water storage (mm)
    storage = 75.0

    # Maximum soil-water storage (mm)
    max_storage = 150.0

    storage_series = []
    evapotranspiration_series = []
    drainage_series = []

    for rain, temp in zip(rainfall, temperature):

        # Potential evapotranspiration
        pet = max(0, 0.7 + 0.04 * temp)

        # Vegetation water demand
        et_demand = pet * vegetation_factor

        # Add rainfall
        storage += rain

        # Actual ET cannot exceed available soil water
        actual_et = min(storage, et_demand)

        storage -= actual_et

        # Drainage when storage exceeds field capacity
        drainage = max(0, storage - max_storage)

        storage -= drainage

        storage_series.append(storage)
        evapotranspiration_series.append(actual_et)
        drainage_series.append(drainage)

    return (
        np.array(storage_series),
        np.array(evapotranspiration_series),
        np.array(drainage_series)
    )


# --------------------------------------------------
# 3. Vegetation scenarios
# --------------------------------------------------

scenarios = {
    "bare": 0.8,
    "moderate": 1.0,
    "high": 1.3
}


# --------------------------------------------------
# 4. Run simulations
# --------------------------------------------------

for name, vegetation_factor in scenarios.items():

    storage, et, drainage = run_model(
        rainfall,
        temperature,
        vegetation_factor
    )

    df[f"{name}_storage_mm"] = storage
    df[f"{name}_ET_mm"] = et
    df[f"{name}_drainage_mm"] = drainage


# --------------------------------------------------
# 5. Save results
# --------------------------------------------------

output_path = Path("data/soil_water_results.csv")

df.to_csv(output_path, index=False)

print("Soil-water model completed.")
print(f"Results saved to: {output_path}")

print("\nModel summary:")

for name in scenarios:

    mean_storage = df[f"{name}_storage_mm"].mean()
    total_drainage = df[f"{name}_drainage_mm"].sum()

    print(
        f"{name}: "
        f"mean storage = {mean_storage:.2f} mm, "
        f"total drainage = {total_drainage:.2f} mm"
    )