# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Correct file name
# df = pd.read_csv("WomenDressesReviewsDataset")

# print(df.head())

# sns.set_style("whitegrid")

# # 1 Rating Distribution
# plt.figure(figsize=(8,5))
# sns.countplot(x="Rating", data=df)
# plt.title("Rating Distribution")
# plt.show()

# # 2 Age Distribution
# plt.figure(figsize=(8,5))
# sns.histplot(df["Age"], bins=20)
# plt.title("Age Distribution")
# plt.show()

# # 3 Department Reviews
# plt.figure(figsize=(10,6))
# sns.countplot(y="Department Name", data=df)
# plt.title("Reviews by Department")
# plt.show()

# # 4 Product Type
# plt.figure(figsize=(10,6))
# sns.countplot(y="Class Name", data=df)
# plt.title("Most Reviewed Products")
# plt.show()

# # 5 Age vs Rating
# plt.figure(figsize=(8,5))
# sns.scatterplot(x="Age", y="Rating", data=df)
# plt.title("Age vs Rating")
# plt.show()


#  AGE vs RATING


plt.figure(figsize=(8,5))

sns.scatterplot(x="Age", y="Rating", data=df)

plt.title("Age vs Rating")

plt.show()


# RECOMMENDATION COUNT


plt.figure(figsize=(6,4))

sns.countplot(x="Recommended IND", data=df)

plt.title("Recommendation Distribution")

plt.show()


# AVERAGE RATING BY DEPARTMENT


plt.figure(figsize=(8,5))

sns.barplot(x="Department Name", y="Rating", data=df)

plt.title("Average Rating by Department")

plt.show()

#  HEATMAP CORRELATION


plt.figure(figsize=(8,6))

sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title("Correlation Heatmap")

plt.show()