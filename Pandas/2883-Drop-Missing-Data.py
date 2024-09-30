import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset="name")
    # df.dropna() remove duplicates with missing value.
    # df here means the name of your DataFrame as in my 3rd line(students).