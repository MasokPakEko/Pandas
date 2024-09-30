import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary*=2
    return employees

"""
another code
    up_salary = employees['salary']*2
    employees.update(up_salary)
    return employees

another one
    employees["salary"] = employees["salary"]*2
    return employees
"""