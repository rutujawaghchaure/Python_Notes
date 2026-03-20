

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")

print("Dataset Shape:", df.shape)
print(df.head())



df = df.dropna()

print("\nAfter Cleaning:", df.shape)


# RATING DISTRIBUTION


plt.figure(figsize=(8,5))

sns.countplot(x="Rating", data=df)

plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")


plt.xticks(
    [0,1,2,3,4],
    ["1 → Very Bad", "2 → Bad", "3 → Average", "4 → Good", "5 → Excellent"]
)

plt.show()


#  AGE DISTRIBUTION


plt.figure(figsize=(8,5))

sns.histplot(df["Age"], bins=20)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")

plt.show()









#  TOP CLOTHING PRODUCTS


plt.figure(figsize=(10,6))

ax = sns.countplot(
    x="Class Name",
    data=df,
    order=df["Class Name"].value_counts().index,
    palette="viridis"
)

plt.title("Most Reviewed Clothing Products", fontsize=14)
plt.xlabel("Clothing Product Type")
plt.ylabel("Number of Reviews")

# bar ke upar numbers
for p in ax.patches:
    ax.text(
        p.get_x() + p.get_width()/2,
        p.get_height() + 20,
        int(p.get_height()),
        ha="center"
    )

plt.xticks(rotation=45)

plt.show()




