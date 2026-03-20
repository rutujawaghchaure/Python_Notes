# # import pandas 

# # mydataset = {
# #   'cars': ["BMW", "Volvo", "Ford"],
# #   'passings': [3, 7, 2]
# # }

# # myvar = pandas.DataFrame(mydataset)

# # print(myvar)
# # A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.


# # import pandas as pd

# # a = [1, 7, 2]

# # myvar = pd.Series(a)

# # print(myvar)
# # print(myvar[0])

# # import pandas as pd

# # a = [1, 7, 2]

# # myvar = pd.Series(a, index = ["x", "y", "z"])

# # print(myvar)

# # datafream

# # import pandas as pd

# # data = {
# #   "calories": [420, 380, 390],
# #   "duration": [50, 40, 45]
# # }

# # #load data into a DataFrame object:
# # df = pd.DataFrame(data)

# # print(df) 
# # print(df.loc[0])
# # import pandas as pd

# # data = {
# #   "calories": [420, 380, 390],
# #   "duration": [50, 40, 45]
# # }

# # df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# # print(df)


# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # print(df) 

# import pandas as pd

# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')

# print(df) 

# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # new_df = df.dropna()

# # print(new_df.to_string())

# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # df.dropna(inplace = True)

# # print(df.to_string())

# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # df.fillna(130, inplace = True)
# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# # print(df.to_string())

# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # df['Date'] = pd.date_range(start='2025-02-01', periods=len(df))

# # print(df)
# # s.display.max_rows)


# datatypes in pandas
# series - 1d labelled array
# dataframe 2d labelled array




# import pandas as pd
# info={
#     "name":["rutuja","jigar","chotu"],
#     "roll":[89,876,56]
# }

# df=pd.DataFrame(info,index=["a","b","c"])
# print(df)


# import pandas as pd

# s = pd.Series([4,6,8,3], index=["aa","bb","cc","dd"])
# print(s)

# s1=pd.Series([1,2,3,4])
# s2=pd.Series([3,5,6,7])
# print(s1 + s2)

# info={
#     "name":["aa","dd","cc","xx"],
#     "age":[2,4,5,6]
# }
# df=pd.DataFrame(info)
# print(df)


# import pandas as pd
# df=pd.read_csv("employee_data.csv")
# df.tail(2)

# print(df,type(df))


import pandas as pd

mydataset={
    "id":[1,2,3,4,5,5,7,8,9,10],
    "name":["rutu","chotu","jigar","rutuja","poojan","isha","Amit","Niket","Rahul","virat"],
    "Age":[20,22,23,22,21,24,25,26,26,30],
    "roll_no":[11,12,13,14,15,16,17,18,19,20],
    "DOB":["20/04/2004","25/04/2005","12/02/2005","21/03/2003","11/03/2005","27/02/2005","10/11/2009","12/01/2006","18/07/2005","12/12/2003"],
    "Gender": ["Female","Male","Male","Female","Male","Female","Male","Male","Male","Male"],
    "Phoneno": [9876543210,9876501234,9876512345,9876523456,9876534567,
                9876545678,9876556789,9876567890,9876578901,9876589012],
    
    "english_marks": [None,65,80,72,72,88,75,90,60,85],
    "maths_marks": [85,70,88,76,74,92,81,95,66,89],
    "computer_marks": [90,75,85,80,78,94,83,96,70,91],
    "total": [253, 210, 253, 228, 221, 274, 239, 281, 265, 265],
"percentage": [84.33, 70.00, 84.33, 76.00, 73.67, 91.33, 79.67, 93.67, 65.33, 88.33],
"grade": ["A", "B", "A", "B", "B", "A", "B", "A", "B", "A"],
 "id":[1,2,3,4,5,5,7,8,9,10],
"result": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]


}

df=pd.DataFrame(mydataset)
# print(df)

print(df.head())
print(df["total"].mean())
print(df["total"].median())
print(df["total"].mode())
print(df.isnull().sum())
print(df.tail())
print(df.tail(1))


print(df.shape)
print(df.describe())
print(df.fillna(0, inplace=True))
print(df.dropna())
print(df.duplicated())

# print(df[(df["Age"] > 25) & (df["grade"] == "A")])
# print(df[(df["total"]>200)])


for x in df.index:
  if df.loc[x, "total"] > 200:
    df.loc[x, "total"] = 300
print(df)





