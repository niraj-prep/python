import pandas as pd
import os

EXCEL_FILE = 'employee.xlsx'

def create_sample_excel():
    sample = {
        'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'Employee_Name': [
            'Amit Sharma', 'Priya Patel', 'Rahul Verma',
            'Sneha Joshi', 'Vikram Singh', 'Anjali Nair',
            'Deepak Gupta', 'Kavita Rao',  'Suresh Iyer', 'Meera Pillai'
        ],
        'Department': [
            'Automotive', 'Finance',     'Automotive',
            'Healthcare', 'Automotive',  'BFS',
            'Retail',     'Automotive',  'Telecom',   'Healthcare'
        ],
        'Designation': [
            'Developer',        'Analyst',          'Developer',
            'Senior Developer', 'Team Lead',        'Developer',
            'Manager',          'Developer',        'Consultant', 'Analyst'
        ],
        'Experience_Years': [3, 5, 2, 7, 10, 4, 8, 6, 9, 3],
        'Salary': [
            55000, 62000, 48000, 85000, 110000,
            60000, 95000, 72000, 105000, 50000
        ],
        'Location': [
            'Pune', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai',
            'Delhi', 'Kolkata', 'Pune', 'Mumbai', 'Bangalore'
        ],
    }
    pd.DataFrame(sample).to_excel(EXCEL_FILE, index=False)
    print(f"[INFO] '{EXCEL_FILE}' not found – created a sample file.\n")

if not os.path.exists(EXCEL_FILE):
    create_sample_excel()

df = pd.read_excel(EXCEL_FILE)

print("=" * 60)
print("         Infosys Software Solutions – Employee Data")
print("=" * 60)
print(df.to_string(index=False))
print()

print("─" * 55)
print('a) Employees Working in "Automotive" Domain')
print("─" * 55)
automotive = df[df['Department'].str.strip().str.lower() == 'automotive']
if automotive.empty:
    print("  No employees found in Automotive domain.")
else:
    print(automotive.to_string(index=False))
print()

print("─" * 55)
print("b) Search Employee by ID")
print("─" * 55)
try:
    emp_id = int(input("   Enter Employee ID to search: ").strip())
    result = df[df['Employee_ID'] == emp_id]
    if result.empty:
        print(f"  No employee found with ID {emp_id}.")
    else:
        print("\n  Employee Details:")
        print("  " + "-" * 45)
        for col in result.columns:
            print(f"  {col:<20}: {result[col].values[0]}")
except ValueError:
    print("  Invalid input. Please enter a numeric Employee ID.")
print()

print("─" * 55)
print("d) List of All Developers at Infosys")
print("─" * 55)
developers = df[df['Designation'].str.strip().str.lower().str.contains('developer')]
if developers.empty:
    print("  No developers found.")
else:
    print(developers.to_string(index=False))
print()