import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    newest_data = employees.head(3) # number indicates how many rows to show
    return(newest_data)