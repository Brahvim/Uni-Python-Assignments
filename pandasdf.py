import pandas as pd


def log(p_text, p_object):
    print(f"{p_text}\n{p_object}", end="\n\n")


data = {
    "age": ["10", "20", "30"],
    "city": ["KTW", "NDA", "DLH"],
    "gender": ["male", "male", "female"],
    "name": ["Brahvim", "Akash", "Chitra"],
}

df = pd.DataFrame(data)
log("Value of `df`:", df)
df.to_csv("./files/pandasdf.csv")
df.to_excel("./files/pandasdf.xlsx")

studs = pd.read_csv("./files/pandasdf.csv")
log("Value of `studs`:", studs)
log("Value from `studs::head()`:", studs.head())
log("Value from `studs::tail()`:", studs.tail())
log("Value from `studs::head(10)`:", studs.head(10))
log("Value from `studs::info()`:", studs.info())
log("Value of `studs::shape`:", studs.shape)
log("Value of `studs::describe()`:", studs.describe())
log("Value of `studs::[:]`:", studs.loc[:])
log("Value of `studs::[:2]`:", studs.loc[:1])  # That `1` is INCLUSIVE!!!
log("Value of `studs::[-1:2]`:", studs.loc[-3:0])  # Missing rows are omitted.
log("Value of `studs::[studs[\"age\"] < 25]`:",
    studs.loc[studs["age"] < 25])  # Filtering!
# Nope! No `str`-manip!:
# log("Value of `studs::[studs[\"age\"] < 25]`:", studs.loc[str(studs["name"]).lower().startswith("a") & studs["gender"] == "male"])
log("Complex query:", studs.query(
    "name.str.startswith('A').values")[studs["age"] < 25])
