employees = {
 'E001': {'name': 'Alice', 'department': 'HR', 'salary': 50000},
 'E002': {'name': 'Bob', 'department': 'IT', 'salary': 60000},
 'E003': {'name': 'Charlie', 'department': 'Finance', 'salary': 55000}
}
def get_salary(employee_dict,emp_id):
    return employee_dict.get(emp_id,{}).get('salary',"Salary not found")
def increase_salary(employee_dict,percentage):
    for emp in employee_dict.values():
        emp['salary']+=emp['salary']*percentage/100
increase_salary(employees,5)
print(employees)