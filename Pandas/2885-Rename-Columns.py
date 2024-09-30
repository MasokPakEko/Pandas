import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={
        'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        'age':'age_in_years'
    }, inplace=True) # Ensures that the DataFrame is modified in place/changes are applied directly to the original DataFrame.
    return students # Need to include if you put inplace=True

""" return students.rename(columns={
    'id': 'student_id',
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'
    })
"""
