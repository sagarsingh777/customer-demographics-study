import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

df = pd.read_csv("data/customer_data.csv")

# 1. Age distribution
plt.figure(figsize=(9,5))
sns.histplot(df["Age"], bins=20, kde=True, color="#4F46E5")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.tight_layout()
plt.savefig("charts/01_age_distribution.png")
plt.close()

# 2. Gender split
plt.figure(figsize=(6,6))
gender_counts = df["Gender"].value_counts()
plt.pie(gender_counts.values, labels=gender_counts.index, autopct="%1.1f%%",
        colors=["#4F46E5", "#EC4899", "#10B981"], startangle=90)
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("charts/02_gender_distribution.png")
plt.close()

# 3. Customers by city
plt.figure(figsize=(9,5))
city_counts = df["City"].value_counts()
sns.barplot(x=city_counts.values, y=city_counts.index, hue=city_counts.index, palette="viridis", legend=False)
plt.title("Customers by City")
plt.xlabel("Number of Customers")
plt.tight_layout()
plt.savefig("charts/03_customers_by_city.png")
plt.close()

# 4. Income bracket distribution
plt.figure(figsize=(8,5))
income_order = ["<25k", "25k-50k", "50k-100k", "100k-200k", "200k+"]
income_counts = df["IncomeBracket"].value_counts().reindex(income_order)
sns.barplot(x=income_counts.index, y=income_counts.values, hue=income_counts.index, palette="mako", legend=False)
plt.title("Customer Income Bracket Distribution")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("charts/04_income_distribution.png")
plt.close()

# 5. Avg spend by membership tier
plt.figure(figsize=(8,5))
tier_order = ["Basic", "Silver", "Gold", "Platinum"]
tier_spend = df.groupby("MembershipTier")["AnnualSpend"].mean().reindex(tier_order)
sns.barplot(x=tier_spend.index, y=tier_spend.values, hue=tier_spend.index, palette="flare", legend=False)
plt.title("Average Annual Spend by Membership Tier")
plt.ylabel("Avg Annual Spend ($)")
plt.tight_layout()
plt.savefig("charts/05_spend_by_membership.png")
plt.close()

# 6. Education vs Income (heatmap)
plt.figure(figsize=(8,6))
edu_order = ["High School", "Bachelor's", "Master's", "PhD"]
cross = pd.crosstab(df["Education"], df["IncomeBracket"]).reindex(edu_order)[income_order]
sns.heatmap(cross, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Education Level vs Income Bracket")
plt.tight_layout()
plt.savefig("charts/06_education_vs_income.png")
plt.close()

print("Charts generated.")
print("\n--- Summary Stats ---")
print(f"Total Customers: {len(df):,}")
print(f"Avg Age: {df['Age'].mean():.1f}")
print(f"Avg Annual Spend: ${df['AnnualSpend'].mean():,.2f}")
print(f"Top City: {city_counts.index[0]} ({city_counts.iloc[0]} customers)")
print(f"Gender Split: {dict(gender_counts)}")
