import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

# --------------------------------------------------
# 1. Five years of daily climate data
# --------------------------------------------------

dates = pd.date_range(
    start="2021-01-01",
    end="2025-12-31",
    freq="D"
)

n = len(dates)
day_of_year = dates.dayofyear.values


# --------------------------------------------------
# 2. Seasonal rainfall
# --------------------------------------------------

# Wet season centered around day 210
seasonal_factor = np.exp(
    -((day_of_year - 210) / 70) ** 2
)

rainfall_probability = (
    0.18 + 0.30 * seasonal_factor
)

rain_occurs = np.random.random(n) < rainfall_probability

rainfall = np.zeros(n)

rainfall[rain_occurs] = np.random.gamma(
    shape=1.5,
    scale=7.0,
    size=rain_occurs.sum()
)


# --------------------------------------------------
# 3. Controlled drought period
# --------------------------------------------------

drought_start = pd.Timestamp("2023-06-01")
drought_end = pd.Timestamp("2023-09-30")

drought_mask = (
    (dates >= drought_start)
    & (dates <= drought_end)
)

rainfall[drought_mask] *= 0.02


# --------------------------------------------------
# 4. Rainfall recovery
# --------------------------------------------------

recovery_start = pd.Timestamp("2023-10-01")
recovery_end = pd.Timestamp("2023-10-31")

recovery_mask = (
    (dates >= recovery_start)
    & (dates <= recovery_end)
)

rainfall[recovery_mask] *= 2.5


# --------------------------------------------------
# 5. Temperature
# --------------------------------------------------

temperature = (
    15
    + 10 * np.sin(
        2 * np.pi * (day_of_year - 80) / 365
    )
    + np.random.normal(0, 2, n)
)


# --------------------------------------------------
# 6. Save climate dataset
# --------------------------------------------------

df = pd.DataFrame({
    "date": dates,
    "rainfall_mm": rainfall,
    "temperature_C": temperature
})

output_path = Path("data/synthetic_climate.csv")

df.to_csv(output_path, index=False)

print("Synthetic climate dataset created.")
print(f"Period: {dates.min().date()} to {dates.max().date()}")
print(f"Number of days: {len(df)}")
print(f"Total rainfall: {rainfall.sum():.1f} mm")
print(f"Mean daily rainfall: {rainfall.mean():.2f} mm")
print(f"Maximum daily rainfall: {rainfall.max():.1f} mm")
print(
    f"Drought rainfall "
    f"({drought_start.date()} to {drought_end.date()}): "
    f"{rainfall[drought_mask].sum():.1f} mm"
)