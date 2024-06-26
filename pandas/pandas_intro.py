# -*- coding: utf-8 -*-
"""pandas_intro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10F2Rd62vra3uK4HtJepDtnq4pYqJh-tp

# **Learning Pandas**
"""

from google.colab import drive

drive.mount("/content/drive")

import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Rahul",
            "Anil",
            "Mahesh",
            "Ravi",
        ],
        "College": ["uvpce", "skpcer", "bsp", "vpce"],
        "Age": [18, 19, 21, 20],
    }
)

df

df["Name"]

location = pd.Series(["ahmedabad", "gandhinagar", "amreli", "surat"], name="Address")

location

df["Age"].max()

df.describe()

dt = pd.read_csv("/content/drive/MyDrive/data_practices/pandas/titanic.csv")

dt

dt.describe()

dt.head()

dt.tail(8)

dt.dtypes

dt.to_excel("titanic.xlsx", sheet_name="titanic_spreadsheet", index=False)

excel = pd.read_excel("titanic.xlsx")
excel

print(excel["Age"].max())

dt.info()

base_info = dt[["Name", "Sex", "Age"]]
base_info

base_info.max()

"""**How do I select a subset of a DataFrame?**"""

base_info["Name"].shape

type(dt["Age"])

base_info.head()

dt[["Age", "Sex"]].shape

dt

# male = dt["Sex"]=="male"
male = dt[dt["Sex"] == "male"]
male

age_lessthan_50 = dt[dt["Age"] < 50]
age_lessthan_50

age_lessthan_50.shape

"""> isin() conditional function

"""

class_23 = dt[dt["Pclass"].isin([2, 3])]
class_23.head(8)

"""When combining multiple conditional statements, each condition must be surrounded by parentheses (). Moreover, you can not use or/and but need to use the or operator | and the and operator &.



"""

between_ages = dt[(dt["Age"] > 18) & (dt["Sex"] == "male")]
between_ages.head()

age_between = dt[(dt["Age"].between(20, 35)) & (dt["Sex"] == "female")]
age_between.head()

"""

```
# Removing Null columns for cabin and age
```

"""

dt.info()

"""

```
# notna() conditional function returns a True for each row the values are not a Null value.
```

"""

not_null_age_cabin = dt[dt["Age"].notna() & dt["Cabin"].notna()]
not_null_age_cabin.head()

"""**When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.**"""

loc_ages = dt.loc[dt["Age"] > 70, "Sex"]
print(loc_ages.head())
loc_1 = dt.loc[4, "Age"]
print("loc_1: ", loc_1)

"""**Select specific rows and/or columns using iloc when using the positions in the table.**"""

rows_cols = dt.iloc[15:23, 3:6]
rows_cols

dt.iloc[0:3, 3] = "no name"
dt.head()
