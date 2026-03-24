import pandas as pd

data = {
    "State": [
        "Maharashtra",
        "Rajasthan",
        "Uttar Pradesh",
        "Madhya Pradesh",
        "Tamil Nadu",
    ],
    "Area_km2": [307713, 342239, 240928, 308252, 130058],          # km²
    "Population": [112374333, 68548437, 199812341, 72626809, 72147030],
}

df = pd.DataFrame(data)

# Compute population density (people per km²)
df["Pop_Density"] = (df["Population"] / df["Area_km2"]).round(2)

print("=" * 65)
print("  a) Complete Information of States")
print("=" * 65)
print(df.to_string(index=False))
print()

print("=" * 65)
print("  b) State with Largest Area")
print("=" * 65)
largest_area = df.loc[df["Area_km2"].idxmax()]
print(f"  {largest_area['State']}  —  {largest_area['Area_km2']:,} km²")
print()

print("=" * 65)
print("  c) State with Largest Population")
print("=" * 65)
largest_pop = df.loc[df["Population"].idxmax()]
print(f"  {largest_pop['State']}  —  {largest_pop['Population']:,}")
print()

print("=" * 65)
print("  d) Population Density of Each State  (people / km²)")
print("=" * 65)
print(df[["State", "Pop_Density"]].to_string(index=False))
print()

print("=" * 65)
print("  e) State with Highest Population Density")
print("=" * 65)
highest_density = df.loc[df["Pop_Density"].idxmax()]
print(f"  {highest_density['State']}  —  {highest_density['Pop_Density']} people/km²")
print()