# Pandas3

# 1 Problem 1 :Calculate Special Bonus ( https://leetcode.com/problems/calculate-special-bonus/)

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] %2 ==1 and not x['name'].startswith('M') else 0, axis =1)
    return employees[['employee_id','bonus']].sort_values(by = ['employee_id'])

# 2 Problem 2 : Fix Names in a Table	(	https://leetcode.com/problems/fix-names-in-a-table/ )

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # users['name'] = users['name'].str.capitalize()
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by=['user_id'])

# 3 Problem 3 : Patients with a Condition ( https://leetcode.com/problems/patients-with-a-condition/)

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    return df