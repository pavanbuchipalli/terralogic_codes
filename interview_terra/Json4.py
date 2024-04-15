# # nalyze JSON Data and Perform,
# # design a sample JSON file containing information about (min10) employees in a company.
# # implement the following operations based on the given requirements:
# # 1)Calculate the average salary of all employees.
# # 2)Find the employee with the highest salary and display their details (name, department, and salary).
# # 3)Identify the projects that are being worked on by at least two employees
import json
import pandas as pd
f  = open("Task3.json", "r")
data = f.read()
json_data=json.loads(data)
c=json_data["employess"]

# for i in c:
#     print(i)

data_test ={
    'Name':[],
    'Department':[],
    'Salary' : [],
    "project": []

}
for i in range(len(c)):
    name = c[i].get("Name")
    data_test['Name'].append(name)
    Department =c[i].get("Department")
    data_test['Department'].append(Department)
    Salary=  c[i].get("Salary")
    data_test['Salary'].append(Salary)
    project = c[i].get("project")
    data_test['project'].append(project)

df_test = pd.DataFrame(data_test)
print(df_test)
projectss = df_test.get("project")
# print(projectss)

print("----------------------------------------------------------------------------------------------------------------")
# to find the average of the salary
salary_s = df_test.get("Salary")

total_salary = 0
lenght_ = len(salary_s)
for salary  in salary_s:
    total_salary += salary

print("Average of total salaries of employess is",total_salary/lenght_)
print("------------------------------------------------------------------------------------------------------------------")

# to find the index of the max number in dataframe
maximum =df_test['Salary'].idxmax()

print("The index number of employess with max salary",    maximum)

print("---------------------------------------------------------------------------------------------------------------------")

#  to find extact the entire row which contains max_number
print("Here is the list of  employess with highest salary")
row_of_max_salary =df_test.query('Salary == Salary.max()')
print(row_of_max_salary)
print("---------------------------------------------------------------------------------------------------------------------")

#  To print count of occarence of each project
project = df_test.get("project")
val =pd.Series(project)
occurrences = val.value_counts()
print("list of count of occarence of project",occurrences)
print("---------------------------------------------------------------------------------------------------------------------")


# to print only row with occarence of project more than 2 times

print(df_test[df_test['project'].str.contains('LPU|Psu')])


