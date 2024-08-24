import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
n_students = 100
student_ids = range(1000, 1000 + n_students)
ages = np.random.randint(18, 25, n_students)
gpas = np.round(np.random.uniform(2.0, 4.0, n_students), 2)
majors = np.random.choice(['Computer Science', 'Biology', 'Physics', 'Mathematics', 'Engineering', 'Chemistry'], n_students)

# Create DataFrame
df = pd.DataFrame({
    'student_id': student_ids,
    'age': ages,
    'gpa': gpas,
    'major': majors
})

# Save to CSV
df.to_csv('student_data.csv', index=False)

print("CSV file 'student_data.csv' has been generated.")