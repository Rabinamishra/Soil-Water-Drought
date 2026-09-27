import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load results
df = pd.read_csv("data/soil_water_results.csv")
df["date"] = pd.to_datetime(df["date"])

# Focus on drought + recovery period
period = df[
    (df["date"] >= "2023-05-01") &
    (df["date"] <= "2023-11-30")
]

plt.figure(figsize=(11, 6))

plt.plot(
    period["date"],
    period["bare_storage_mm"],
    label="Bare soil"
)

plt.plot(
    period["date"],
    period["moderate_storage_mm"],
    label="Moderate vegetation"
)

plt.plot(
    period["date"],
    period["high_storage_mm"],
    label="High vegetation"
)

# Drought period
plt.axvspan(
    pd.Timestamp("2023-06-01"),
    pd.Timestamp("2023-09-30"),
    alpha=0.2,
    label="Drought"
)

# Recovery period
plt.axvspan(
    pd.Timestamp("2023-10-01"),
    pd.Timestamp("2023-10-31"),
    alpha=0.12,
    label="Recovery"
)

plt.xlabel("Date")
plt.ylabel("Soil-water storage (mm)")
plt.title("Simulated soil-water storage during drought and recovery")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

output_path = Path("figures/drought_recovery_storage.png")

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Figure saved to: {output_path}")