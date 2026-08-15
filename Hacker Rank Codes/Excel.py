# Create Excel file with questions and solutions from the PDF

from openpyxl import Workbook

wb = Workbook()

# Sheet 1: Questions
ws1 = wb.active
ws1.title = "Questions"

questions = [
"Create a Pivot Table from the given data: Employee, Department, Salary",
"Show Total Salary by Department",
"Add a Filter by Employee Name",
"Group Salaries into ranges (0–50k, 50k–100k)",
"Show Average Salary by Department",
"Show Total Salary by Department and by Employee",
"Insert a Pivot Chart for salary distribution",
"Show Maximum Salary in each Department",
"Show Minimum Salary in each Department",
"Count Number of Employees in each Department",
"Show Salary distribution by Department and Salary Ranges",
"Filter Pivot Table to show only HR Department",
"Add a Slicer for Department",
"Sort Departments by Total Salary (Descending)",
"Create a Pivot Chart showing Average Salary by Department"
]

ws1.append(["Task No.", "Task Description"])

for i, q in enumerate(questions, start=1):
    ws1.append([i, q])


# Sheet 2: Solutions
ws2 = wb.create_sheet(title="Solutions")

solutions = [
"Insert → Pivot Table → Select dataset → New Worksheet",
"Drag Department → Rows, Salary → Values (Sum)",
"Drag Employee → Filters",
"Right-click Salary → Group → 0–100000, interval 50000",
"Change Salary Values → Average",
"Rows: Department + Employee → Values: Sum",
"Insert → Pivot Chart → Column Chart",
"Change Salary Values → Max",
"Change Salary Values → Min",
"Drag Employee → Values (Count)",
"Rows: Department + Salary Groups",
"Filter Department → Select HR",
"Insert → Slicer → Department",
"Sort → Largest to Smallest",
"Insert → Pivot Chart → Average Salary"
]

ws2.append(["Task No.", "Solution"])

for i, s in enumerate(solutions, start=1):
    ws2.append([i, s])


# Save file
file_path = "/mnt/data/Excel_Lab_Assignment_11.xlsx"
wb.save(file_path)

file_path