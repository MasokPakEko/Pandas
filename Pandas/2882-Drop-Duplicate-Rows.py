import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email")
    # subset(columns where the duplicate is),keep(which one is kept(first,last,false)),inplace(True/False)(permanently performed))