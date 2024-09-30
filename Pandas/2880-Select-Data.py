import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Use boolean indexing to select the row where student_id is 101
    selected_student = students.loc[students['student_id'] == 101, ['name', 'age']]
    return selected_student