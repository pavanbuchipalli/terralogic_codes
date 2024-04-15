# import csv
# from tabulate import tabulate
#
# # Function to search for employee by code and calculate present and absent days
# def search_employee(csv_file, emp_code):
#     present_days = 0
#     absent_days = 0
#     absent_dates = []
#     emp_name = None
#
#     with open(csv_file, mode='r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header rows
#
#         for row in reader:
#             if row[1] == emp_code:  # Assuming code is in the second column
#                 emp_name = row[2]  # Assuming name is in the third column
#                 for i, status in enumerate(row[3:], start=1):
#                     if status == 'P':
#                         present_days += 1
#                     elif status == 'A':
#                         absent_days += 1
#                         absent_dates.append(f"Day {i}")
#                 break
#
#     return emp_name, present_days, absent_days, absent_dates
# #
# # Sample usage
# csv_file = 'data.csv'  # Replace with your CSV file path
# emp_code = 'Cont - 015'  # Replace with the employee code you want to search for
#
# emp_name, present_days, absent_days, absent_dates = search_employee(csv_file, emp_code)
# if emp_name:
#     table = [
#         ["Employee Name", "Present Days", "Absent Days", "Absent Dates"],
#         [emp_name, present_days, absent_days, ", ".join(absent_dates)]
#     ]
#     print(tabulate(table, headers="firstrow", tablefmt="grid"))
# else:
#     print("Employee with code", emp_code, "not found.")
#
# #
# #
# import pandas as pd
# # #
# # # # Load the CSV file into a pandas DataFrame
# df = pd.read_csv("master.csv")
#
# def get_employees_under_manager(manager_id):
#     # Filter the DataFrame based on the provided manager_id
#     employees_under_manager = df[df['Reporting Manager'] == manager_id]
#     return employees_under_manager
#
# # Example: Provide the Reporting Manager ID
# manager_id = "PSI-176"
#
# # Get employees working under the specified manager
# employees_under_manager = get_employees_under_manager(manager_id)
#
# # Print the details of employees under the specified manager
# print("Employees working under Reporting Manager", manager_id, ":")
# print(employees_under_manager)
# #
# # # import pandas as pd
# # #
# # # # Load the CSV file into a pandas DataFrame
# # # df = pd.read_csv("master.csv")
# # #
# # # def get_employees_under_manager(manager_id):
# # #     # Filter the DataFrame based on the provided manager_id
# # #     employees_under_manager = df[df['Reporting Manager'] == manager_id]
# # #     return employees_under_manager
# # #
# # # # Example: Provide the Reporting Manager ID
# # # manager_id = "PSI-176"
# # #
# # # # Get employees working under the specified manager
# # # employees_under_manager = get_employees_under_manager(manager_id)
# # #
# # # # Print the details of employees under the specified manager
# # # print("Employees working under Reporting Manager", manager_id, ":")
# # # print(employees_under_manager)
# # #
# # # # Extract only Employee Code and print as a list
# # # employee_codes = employees_under_manager['Employee Code'].tolist()
# # # print("\nEmployee Codes:")
# # # for code in employee_codes:
# # #     print(code)
# #
# # import pandas as pd
# #
# # # Load the master.csv file into a pandas DataFrame
# # df = pd.read_csv("master.csv")
# #
# # def get_employees_under_manager(manager_id):
# #     # Filter the DataFrame based on the provided manager_id
# #     employees_under_manager = df[df['Reporting Manager'] == manager_id]
# #     return employees_under_manager
# #
# # # Example: Provide the Reporting Manager ID
# # manager_id = "PSI-176"
# #
# # # Get employees working under the specified manager
# # employees_under_manager = get_employees_under_manager(manager_id)
# #
# # # Print the details of employees under the specified manager
# # print("Employees working under Reporting Manager", manager_id, ":")
# # print(employees_under_manager)
# #
# # # Load the data.csv file into a pandas DataFrame, skipping rows based on header identification
# # data_df = pd.read_csv("data.csv", skiprows=lambda x: x in [0, 1, 2, 3, 4])
# #
# # # Extract employee codes from the previously obtained DataFrame
# # employee_codes = employees_under_manager['Employee Code'].tolist()
# #
# # # Print the count of P and A values for each employee found in data.csv
# # for code in employee_codes:
# #     # Search for the employee code in the data.csv DataFrame
# #     employee_row = data_df[data_df['Code'] == code]
# #
# #     # Check if the employee code exists in data.csv
# #     if not employee_row.empty:
# #         # Calculate the count of 'P' and 'A' values
# #         p_count = employee_row.iloc[0, 3:27].tolist().count('P')
# #         a_count = employee_row.iloc[0, 27:51].tolist().count('A')
# #
# #         print("\nEmployee Code:", code)
# #         print("Count of P values:", p_count)
# #         print("Count of A values:", a_count)
# #     else:
# #         print("\nEmployee Code:", code)
# #         print("Employee details not found in data.csv")
# #




c = "psi-433"pr
r =c.split("-")
print(r[0]+" "+"-"+" "+r[1])