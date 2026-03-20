import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick 


df = pd.read_csv("global_house_purchase_dataset.csv")


type_counts = df['property_type'].value_counts().reset_index()
type_counts.columns = ['property_type', 'count']


sns.set_style("whitegrid")


plt.figure(figsize=(8,5))
sns.barplot(
    data=type_counts,
    x='property_type',
    y='count',
    palette='viridis'   
)

plt.title("Most Demanded Property Types", fontsize=14)
plt.xlabel("Property Type", fontsize=12)
plt.ylabel("Number of Purchases", fontsize=12)

plt.xticks(rotation=45)


for i, v in enumerate(type_counts['count']):
    plt.text(i, v + 1, str(v), ha='center', fontsize=10)

plt.tight_layout()
plt.show()



top_countries = df['country'].value_counts().head(10).index
df_top = df[df['country'].isin(top_countries)]


sns.set_style("whitegrid")


plt.figure(figsize=(10,6))
sns.countplot(
    data=df_top,
    x='country',
    hue='property_type',
    palette='Set2'
)

plt.title("Property Type Distribution Across Top Countries", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Number of Purchases")

plt.xticks(rotation=45)

plt.legend(title="Property Type")
plt.tight_layout()
plt.show()






df['price'] = df['price'] * 1000000


sns.set_style("whitegrid")


plt.figure(figsize=(10,6))
sns.barplot(data=df, x='country', y='price', palette='viridis')

plt.title("Actual House Prices by Country", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Price", fontsize=12)

plt.xticks(rotation=45)


plt.gca().yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'{int(x):,}')
)

plt.tight_layout()
plt.show()
print(df['price'].head())




df = pd.read_csv("global_house_purchase_dataset.csv")

lowest_salary_df = df.nsmallest(10, "customer_salary")

plt.figure(figsize=(8,5))

sns.scatterplot(
     x="customer_salary",
    y="loan_amount",
    data=lowest_salary_df,
    s=80,                 
    color="teal",         
    edgecolor="black"
)

plt.title("Lowest 10 Salaries vs Loan Amount")
plt.xlabel("Customer Salary")
plt.ylabel("Loan Amount")


for i in range(len(lowest_salary_df)):
    plt.text(
        lowest_salary_df["customer_salary"].iloc[i],
        lowest_salary_df["loan_amount"].iloc[i],
        str(lowest_salary_df["loan_amount"].iloc[i]),
        fontsize=8

    )

plt.show()

df = pd.read_csv("global_house_purchase_dataset.csv")


# top_country = df["country"].value_counts().idxmax()

# df_top = df[df["country"] == top_country]


# top_cities = df_top["city"].value_counts().head(5)

# plt.figure(figsize=(10,5))

# sns.barplot(
#     x=top_cities.values,
#     y=top_cities.index
# )

# plt.title(f"Top Cities in {top_country}")
# plt.xlabel("Number of Houses")
# plt.ylabel("City")

# plt.show()


df = pd.read_csv("global_house_purchase_dataset.csv")


df_india = df[df["country"] == "India"]

top_cities = df_india["city"].value_counts().head(5).index
df_india = df_india[df_india["city"].isin(top_cities)]

plt.figure(figsize=(12,6))

sns.countplot(
    y="city",
    hue="property_type",
    data=df_india
)

plt.title("House Types in Top Cities of India")
plt.xlabel("Count")
plt.ylabel("City")

plt.legend(title="Property Type")
plt.show()



# plt.figure(figsize=(8,5))

# sns.scatterplot(
#     x="customer_salary",
#     y="loan_amount",
#     data=df,
#     s=60
# )

# plt.title(" Loan Amount")
# plt.xlabel("Customer Income")
# plt.ylabel("Loan Amount")

# plt.show()

df = pd.read_csv("global_house_purchase_dataset.csv")


top10 = (
    df.groupby("country")["loan_amount"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top10.index,
    y=top10.values
)

plt.title("Top 10 Countries by Average Loan Amount")
plt.xlabel("Country")
plt.ylabel("Loan Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()




df = pd.read_csv("global_house_purchase_dataset.csv")

lowest10 = (
    df.groupby("country")["customer_salary"]
    .mean()
    .sort_values(ascending=True)
    .head(10)
)

plt.figure(figsize=(10,5))

sns.barplot(
    x=lowest10.index,
    y=lowest10.values
)

plt.title("Top 10 Countries with Lowest Average Salary")
plt.xlabel("Country")
plt.ylabel("Average Salary")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()




df = pd.read_csv("global_house_purchase_dataset.csv")


lowest_countries = (
    df.groupby("country")["customer_salary"]
    .mean()
    .sort_values()
    .head(10)
    .index
)

df_low = df[df["country"].isin(lowest_countries)]

plt.figure(figsize=(8,5))

sns.countplot(
    x="loan_tenure_years",          
    hue="property_type",    
    data=df_low
)

plt.title("Loan Tenure vs Property Type (Lowest Salary Countries)")
plt.xlabel("Loan Tenure (Years)")
plt.ylabel("Count")

plt.legend(title="Property Type")
plt.show()





df = pd.read_csv("global_house_purchase_dataset.csv")

df['price'] = df['price'] * 1000000  

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="property_size_sqft",
    y="price",
    alpha=0.6,           
    color="purple",
    edgecolor="black"
)

plt.title("Property Size vs Price", fontsize=14)
plt.xlabel("Property Size (sqft)", fontsize=12)
plt.ylabel("Price", fontsize=12)


plt.gca().yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'{int(x):,}')
)

plt.tight_layout()
plt.show()

