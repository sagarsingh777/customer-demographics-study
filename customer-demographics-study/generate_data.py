import pandas as pd
import numpy as np

np.random.seed(7)
n = 2500

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad"]
city_weights = [0.18, 0.16, 0.15, 0.10, 0.10, 0.11, 0.10, 0.10]

genders = ["Male", "Female", "Other"]
gender_weights = [0.49, 0.48, 0.03]

income_brackets = ["<25k", "25k-50k", "50k-100k", "100k-200k", "200k+"]
education = ["High School", "Bachelor's", "Master's", "PhD"]
edu_weights = [0.2, 0.45, 0.28, 0.07]

membership = ["Basic", "Silver", "Gold", "Platinum"]

rows = []
for i in range(n):
    age = int(np.clip(np.random.normal(34, 11), 18, 75))
    gender = np.random.choice(genders, p=gender_weights)
    city = np.random.choice(cities, p=city_weights)
    edu = np.random.choice(education, p=edu_weights)

    # income correlates loosely with age & education
    edu_bonus = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 2}[edu]
    income_idx = int(np.clip(np.random.normal(1.5 + edu_bonus*0.4 + (age-18)/57*1.5, 1.0), 0, 4))
    income = income_brackets[income_idx]

    # spend correlates with income bracket
    base_spend = [3000, 8000, 18000, 35000, 60000][income_idx]
    annual_spend = max(500, np.random.normal(base_spend, base_spend*0.3))

    member = np.random.choice(membership, p=[0.4, 0.3, 0.2, 0.1])
    tenure_months = np.random.randint(1, 60)
    orders = max(1, int(np.random.poisson(annual_spend/4000) ))

    rows.append({
        "CustomerID": f"C{1000+i}",
        "Age": age,
        "Gender": gender,
        "City": city,
        "Education": edu,
        "IncomeBracket": income,
        "AnnualSpend": round(annual_spend, 2),
        "MembershipTier": member,
        "TenureMonths": tenure_months,
        "TotalOrders": orders
    })

df = pd.DataFrame(rows)
df.to_csv("data/customer_data.csv", index=False)
print(df.shape)
print(df.head())
