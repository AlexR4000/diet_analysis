import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a folder to save charts
os.makedirs("charts", exist_ok=True)

# Load the dataset
df = pd.read_csv("All_Diets.csv")

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')

# Show dataset overview
print("First 5 rows of the dataset:")
print(df.head(), "\n")
print("Columns in the dataset:")
print(df.columns.tolist(), "\n")

# Fill missing values
for col in ["Protein(g)", "Carbs(g)", "Fat(g)"]:
    df[col] = df[col].fillna(df[col].mean())

# Average macronutrients per diet
avg_macros = df.groupby("Diet_type")[["Protein(g)", "Carbs(g)", "Fat(g)"]].mean().reset_index()
print("Average macronutrients per diet:")
print(avg_macros, "\n")

# Top 5 protein-rich recipes per diet
top_protein = df.sort_values("Protein(g)", ascending=False).groupby("Diet_type", group_keys=False).head(5).reset_index(drop=True)
print("Top 5 protein-rich recipes per diet:")
print(top_protein[["Diet_type", "Recipe_name", "Protein(g)"]], "\n")

# Diet type with highest average protein
highest_protein_diet = avg_macros.loc[avg_macros["Protein(g)"].idxmax()]
print(f"Diet type with highest average protein: {highest_protein_diet['Diet_type']} ({highest_protein_diet['Protein(g)']:.2f} g)\n")

# Most common cuisine per diet
most_common_cuisine = df.groupby("Diet_type")["Cuisine_type"].agg(lambda x: x.value_counts().idxmax()).reset_index()
print("Most common cuisine per diet:")
print(most_common_cuisine, "\n")

# Compute new metrics
df["Protein_to_Carbs_ratio"] = df["Protein(g)"] / df["Carbs(g)"]
df["Carbs_to_Fat_ratio"] = df["Carbs(g)"] / df["Fat(g)"]
print("Sample of new metrics:")
print(df[["Recipe_name", "Protein_to_Carbs_ratio", "Carbs_to_Fat_ratio"]].head(), "\n")

sns.set_style("whitegrid")

# Bars lol

# Bar chart: Average Protein
plt.figure(figsize=(10,6))
sns.barplot(data=avg_macros, x="Diet_type", y="Protein(g)")
plt.title("Average Protein per Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/avg_protein.png")
plt.show()

# Bar chart: Average Carbs
plt.figure(figsize=(10,6))
sns.barplot(data=avg_macros, x="Diet_type", y="Carbs(g)")
plt.title("Average Carbs per Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/avg_carbs.png")
plt.show()

# Bar chart: Average Fat
plt.figure(figsize=(10,6))
sns.barplot(data=avg_macros, x="Diet_type", y="Fat(g)")
plt.title("Average Fat per Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/avg_fat.png")
plt.show()

# Heatmap: Correlation
plt.figure(figsize=(8,6))
corr = df[["Protein(g)", "Carbs(g)", "Fat(g)", "Protein_to_Carbs_ratio", "Carbs_to_Fat_ratio"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png")
plt.show()

# Scatter plot: Top 5 protein-rich recipes
plt.figure(figsize=(10,6))
sns.scatterplot(data=top_protein, x="Carbs(g)", y="Protein(g)", hue="Diet_type", style="Diet_type", s=100)
plt.title("Top 5 Protein-Rich Recipes by Diet Type")
plt.xlabel("Carbs (g)")
plt.ylabel("Protein (g)")
plt.legend()
plt.tight_layout()
plt.savefig("charts/top_protein_recipes.png")
plt.show()