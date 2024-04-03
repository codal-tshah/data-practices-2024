import pandas as pd

df = pd.DataFrame(
    {
        "Name":[
            "Rahul",
            "Anil",
            "Mahesh",
            "Ravi",
        ],
        "College":["uvpce","skpcer","bsp", "vpce"],
        "Age":[18, 19, 21, 20]
    }
)

df

df["Name"]

location = pd.Series(["ahmedabad", "gandhinagar", "amreli", "surat"], name="Address")

location

df["Age"].max()

df.describe()

dt = pd.read_csv("/titanic.csv")

dt

dt.describe()

dt.head()

dt.tail(8)

dt.dtypes

dt.to_excel("new.xlsx", sheet_name="titanic_spreadsheet",index=False)

excel = pd.read_excel("titanic.xlsx")
excel

print(excel["Age"].max())

dt.info()

base_info = dt[["Name", "Sex", "Age"]]
base_info

base_info.max()

base_info["Name"].shape

type(dt["Age"])

base_info.head()