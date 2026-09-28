# Dry-Period Soil–Water Dynamics in a Vegetated Soil Column

## Overview

This project is a computational proof-of-concept investigating how vegetation influences soil-water storage and drainage during a prolonged dry period and subsequent rainfall recovery.

The model represents a simplified soil-water balance:

$$
S_{t+1} = S_t + P - ET - D
$$

where:

* **S** = soil-water storage
* **P** = precipitation
* **ET** = evapotranspiration / vegetation water demand
* **D** = drainage

Three vegetation scenarios are compared:

1. Bare soil
2. Moderate vegetation
3. High vegetation

The objective is to examine how differences in vegetation water demand affect soil-water depletion and drainage under contrasting hydroclimatic conditions.

---

## Synthetic climate forcing

The model uses five years of synthetic daily climate data:

**2021–2025**

The climate dataset contains:

* Daily precipitation
* Daily temperature

A controlled dry period was introduced from:

**1 June–30 September 2023**

A rainfall recovery period was then imposed during:

**1–31 October 2023**

These data are synthetic and are used only to demonstrate the modeling framework.

---

## Model structure

For each day, the model:

1. Adds rainfall to soil-water storage.
2. Estimates potential evapotranspiration from temperature.
3. Applies a vegetation-specific water-demand factor.
4. Subtracts actual evapotranspiration from soil storage.
5. Calculates drainage when storage exceeds the prescribed maximum storage threshold.

The vegetation scenarios use different water-demand factors, allowing the effect of vegetation intensity on soil-water dynamics to be examined.

---

## Main results

The simulations show a clear relationship between vegetation water demand and soil-water storage.

During the imposed dry period, soil-water storage declined substantially in all scenarios. The decline was strongest under greater vegetation water demand, reflecting increased simulated evapotranspiration.

Following rainfall recovery in October 2023, soil-water storage increased again across the scenarios.

Across the full simulation period, total simulated drainage decreased with increasing vegetation intensity:

| Scenario            | Total drainage |
| ------------------- | -------------: |
| Bare soil           |       ~3150 mm |
| Moderate vegetation |       ~2750 mm |
| High vegetation     |       ~2050 mm |

Thus, in this simplified model, greater vegetation water uptake reduced the amount of water remaining available for drainage.

---

## Interpretation

The model demonstrates the basic interaction between precipitation, soil-water storage, vegetation water uptake, and drainage.

The drought experiment highlights an important trade-off:

**greater vegetation water demand can reduce soil-water storage during prolonged dry conditions, while simultaneously reducing the amount of water available for drainage.**

This provides a simple computational framework for examining soil–plant–atmosphere water interactions under hydroclimatic stress.

The results are model outputs rather than field observations.

---

## Relevance to hydrological research

This proof-of-concept provides a starting point for more physically based investigations of:

* Soil-water dynamics
* Vegetation–water interactions
* Drought response and recovery
* Soil-water storage and drainage
* Hydroclimatic variability
* Water residence time and transit processes
* Solute transport in soil systems

A future extension could incorporate measured soil hydraulic properties, vegetation characteristics, soil moisture observations, and tracer or solute transport processes.

---

## Limitations

This is a simplified conceptual model and does not represent a calibrated field-scale hydrological model.

Important limitations include:

* Synthetic precipitation and temperature forcing
* Simplified evapotranspiration formulation
* Fixed soil-water storage capacity
* Simplified representation of vegetation
* No explicit soil hydraulic conductivity
* No root-zone structure
* No measured soil-moisture observations
* No calibration or validation against observations

Therefore, the results should be interpreted as a **computational sensitivity experiment**, not as quantitative predictions of a real soil system.

---

## Project structure

```text
soil_water_drought/
│
├── data/
│   ├── synthetic_climate.csv
│   └── soil_water_results.csv
│
├── figures/
│   ├── soil_water_storage.png
│   ├── drought_recovery_storage.png
│   └── total_drainage_comparison.png
│
├── src/
│   ├── generate_data.py
│   ├── soil_water_model.py
│   ├── plot_storage.py
│   ├── plot_drought_recovery.py
│   ├── plot_drainage.py
│   └── analyze_drought.py
│
├── notebooks/
│
├── README.md
└── requirements.txt
```

## Reproducibility

The project was developed in Python using:

* NumPy
* Pandas
* Matplotlib
* SciPy

The random seed is fixed in the climate-data generation script so that the synthetic climate dataset can be reproduced.

---

## Status

**Computational proof-of-concept completed.**

The project is intended to demonstrate a basic modeling workflow linking hydroclimatic forcing, soil-water storage, vegetation water demand, drought response, and drainage.
