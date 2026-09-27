import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load model results
df = pd.read_csv("data/soil_water_results.csv")

scenarios = ["bare", "moderate", "high"]

drainage = [
    df[f"{scenario}_drainage_mm"].sum()
    for scenario in scenarios
]

labels = [
    "Bare soil",
    "Moderate vegetation",
    "High vegetation"
]

# Plot
plt.figure(figsize=(8, 5))

plt.bar(labels, drainage)

plt.ylabel("Total drainage (mm)")
plt.xlabel("Vegetation scenario")
plt.title("Simulated drainage under different vegetation scenarios")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

output_path = Path("figures/total_drainage_comparison.png")

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Figure saved to: {output_path}")