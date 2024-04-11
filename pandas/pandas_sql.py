# -*- coding: utf-8 -*-
"""Pandas_SQL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ESbFpoHeFF2v5KvACbhT5Hz1csbzt0j0
"""

from google.colab import drive

drive.mount("/content/drive")

"""# **Comparison with SQL**"""

import pandas as pd
import numpy as np

url = (
    "https://raw.githubusercontent.com/pandas-dev"
    "/pandas/main/pandas/tests/io/data/csv/tips.csv"
)

tips = pd.read_csv(url)
tips

tips[["total_bill", "tip", "smoker", "time"]]

"""**DataFrame.assign() method of a DataFrame to append a new column**"""

tips.assign(tip_rate=tips["tip"] / tips["total_bill"])

# old method
# tips["tip_rate"] = tips["tip"]/tips["total_bill"]
# tips

tips["size"].unique()

tips[tips["size"] == 6]

is_dinner = tips["time"] == "Dinner"
is_dinner

is_dinner.value_counts()

sort_by_tip = tips.sort_values("tip")
sort_by_totalbill = tips.sort_values("total_bill", ascending=False)
combine = {"tip": sort_by_tip, "total_bill": sort_by_totalbill}
combine

tips

tips[(tips["sex"] == "Female") & (tips["smoker"] == "Yes") & (tips["tip"] > 4)]

# tips["smoker"].isna().unique()
tips["smoker"].notna()

frame = pd.DataFrame(
    {"col1": ["A", "B", "C", np.nan, "F", "H"], "col2": [1, 8, np.nan, 89, 2, 0]}
)
frame

frame["col2"].isna()

tips.groupby("sex").size()

tips.groupby("sex").count()

tips

tips.groupby("day").agg({"tip": "mean", "day": "size"})

tips.groupby("day").agg({"tip": "mean", "total_bill": "mean"})

tips.groupby(["day", "sex"]).agg({"tip": "mean", "total_bill": "mean"})

tips.groupby(["day", "sex"]).agg({"tip": ["size", "mean"], "total_bill": "mean"})

"""# **JOIN**"""

df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
df2 = pd.DataFrame({"key": ["B", "D", "E", "D"], "value": np.random.randn(4)})

"""merge performs an INNER JOIN by default"""

pd.merge(df1, df2, on="key")

indexed_df2 = df2.set_index("key")
pd.merge(df1, indexed_df2, left_on="key", right_index=True)

pd.merge(df1, df2, on="key", how="right")

pd.merge(df1, df2, on="key", how="right")
