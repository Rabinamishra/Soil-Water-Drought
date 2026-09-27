import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Load model results
# --------------------------------------------------

df = pd.read_csv("data/soil_water_results.csv")

df["date"] = pd.to_datetime(df["date"])


# --------------------------------------------------
# Plot soil-water storage
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["bare_storage_mm"],
    label="Bare soil"
)

plt.plot(
    df["date"],
    df["moderate_storage_mm"],
    label="Moderate vegetation"
)

plt.plot(
    df["date"],
    df["high_storage_mm"],
    label="High vegetation"
)

# Highlight drought period
plt.axvspan(
    pd.Timestamp("2023-06-01"),
    pd.Timestamp("2023-09-30"),
    alpha=0.2,
    label="Drought period"
)

plt.xlabel("Date")
plt.ylabel("Soil-water storage (mm)")
plt.title("Soil-water storage under different vegetation scenarios")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

output_path = Path("figures/soil_water_storage.png")

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Figure saved to: {output_path}")