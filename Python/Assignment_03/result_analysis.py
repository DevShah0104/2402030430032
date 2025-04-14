import pandas as pd

# Load the student marks data from CSV
data = pd.read_csv("students.csv")

# Calculate Total and Percentage
data['Total'] = data[['Math', 'Science', 'English']].sum(axis=1)
data['Percentage'] = (data['Total'] / 300) * 100

# Assign Grade based on Percentage
def assign_grade(percent):
    if percent >= 90:
        return 'A+'
    elif percent >= 80:
        return 'A'
    elif percent >= 70:
        return 'B'
    elif percent >= 60:
        return 'C'
    elif percent >= 50:
        return 'D'
    else:
        return 'F'

data['Grade'] = data['Percentage'].apply(assign_grade)

# Display the full Result Table
print("\n=== Student Result Analysis ===\n")
print(data[['Name', 'Total', 'Percentage', 'Grade']])

# Save the analyzed data to a new CSV
data.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv!")
