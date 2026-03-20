# # # Import seaborn
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# # # Apply the default theme
# # sns.set_theme()

# # # Load an example dataset
# # tips = sns.load_dataset("tips")

# # # Create a visualization
# # sns.relplot(
# #     data=tips,
# #     x="total_bill", y="tip", col="time",
# #     hue="smoker", style="smoker", size="size",
# # )
# # plt.show()

# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # sns.set_theme()

# # tips = sns.load_dataset("tips")

# # sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

# # plt.title("Scatter Plot")
# # plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="dark")

# # tips = sns.load_dataset("tips")   # correct function

# # # sns.relplot(
# # #     data=tips,
# # #     x="total_bill",
# # #     y="tip",
# # #     hue="smoker",
# # #     size="size",
# # #     style="smoker"
# # # )


# # sns.scatterplot(
# #     data=tips,
# #     x="total_bill",
# #     y="tip",
# #     hue="time"

# # )


# tips=sns.load_dataset("tips")
# sns.barplot(
#     data=tips,
#     x="day",
#     y="tip",


# )
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick 

df = pd.read_csv("global_house_purchase_dataset.csv")



df['price'] = df['price'] * 1000000  


top_countries = df['country'].value_counts().head(10).index


df_top10 = df[df['country'].isin(top_countries)]

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df_top10,
    x="property_size_sqft",
    y="price",
    color="blue", 
        
    alpha=0.5
)

plt.title("Property Size vs Price (Top 10 Countries)", fontsize=14)
plt.xlabel("Property Size (sqft)")
plt.ylabel("Price")

plt.gca().yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'{int(x):,}')
)

plt.tight_layout()
plt.show()

df = pd.read_csv("global_house_purchase_dataset.csv")


df = pd.read_csv("global_house_purchase_dataset.csv")

df_india = df[df['country'] == "India"]

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df_india,
    x="property_size_sqft",
    y="price",
    color="blue",
    alpha=0.5
)

plt.title("Property Size vs Price (India)", fontsize=14)
plt.xlabel("Property Size (sqft)")
plt.ylabel("Price")

plt.tight_layout()
plt.show()


df = pd.read_csv("global_house_purchase_dataset.csv")


top10_high_price = (
    df.groupby("country")["price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .index
)

df_top10 = df[df["country"].isin(top10_high_price)]

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df_top10,
    x="property_size_sqft",
    y="price",
    color="blue",
    alpha=0.5
)

plt.title("Property Size vs Price (Top 10 Highest Price Countries)", fontsize=14)
plt.xlabel("Property Size (sqft)")
plt.ylabel("Price")

plt.tight_layout()
plt.show()






df = pd.read_csv("global_house_purchase_dataset.csv")

top10 = (
    df.groupby("country")
    .agg({
        "price": "mean",
        "property_size_sqft": "mean"
    })
    .sort_values(by="price", ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

sns.lineplot(
    x=top10["property_size_sqft"],   
    y=top10["price"],               
    marker='o'
)


for i in range(len(top10)):
    plt.text(
        top10["property_size_sqft"].iloc[i],
        top10["price"].iloc[i],
        top10.index[i],
        fontsize=8
    )

plt.title("Top Countries Avg Size vs Avg Price", fontsize=14)
plt.xlabel("Average Property Size (sqft)")
plt.ylabel("Average Price")

plt.tight_layout()
plt.show()


