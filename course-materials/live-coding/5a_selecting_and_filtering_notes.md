---
title: "Live Coding Session [Instructor Notes]"
subtitle: "Basic Pandas Filtering"
jupyter: eds217_2024
format: 
    html:
        toc: true
        toc-depth: 3
        code-fold: show
---

## Introduction to Pandas Filtering

In this live coding session, we'll explore the fundamental concepts of filtering data in pandas DataFrames. We'll cover logical operations on data values and filtering based on index values.

## Setup

First, let's import pandas and load our dataset.

```{python}
#| echo: true

import pandas as pd

# Load the dataset
df = pd.read_csv('student_data.csv')

# Display the first few rows
print(df.head())

# Display basic information about the DataFrame
print(df.info())
```

## Filtering Based on Column Values

### Single Condition Filtering

Let's start with simple filtering using a single condition.

```{python}
#| echo: true

# Filter students who are 20 years old
students_20 = df[df['age'] == 20]
print(students_20)
```

### Multiple Conditions with Logical Operators

Now, let's combine multiple conditions using logical operators.

```{python}
#| echo: true

# Filter students who are 20 years old AND have a GPA above 3.5
high_performing_20 = df[(df['age'] == 20) & (df['gpa'] > 3.5)]
print(high_performing_20)

# Filter students who are either in Computer Science OR have a GPA above 3.8
cs_or_high_gpa = df[(df['major'] == 'Computer Science') | (df['gpa'] > 3.8)]
print(cs_or_high_gpa)
```

## Filtering on Index Values

Sometimes we might want to filter based on index values. Let's explore this.

```{python}
#| echo: true

# Set 'student_id' as the index
df.set_index('student_id', inplace=True)

# Filter students with IDs between 1000 and 1005
students_1000_1005 = df.loc[1000:1005]
print(students_1000_1005)

# Reset the index
df.reset_index(inplace=True)
```

## Using .isin() for Multiple Values

The `.isin()` method is useful when we want to filter based on multiple possible values.

```{python}
#| echo: true

# Filter students in Computer Science, Biology, or Physics
science_majors = df[df['major'].isin(['Computer Science', 'Biology', 'Physics'])]
print(science_majors)
```

## Filtering with String Methods

Pandas provides string methods that can be used for filtering text data.

```{python}
#| echo: true

# Filter majors that start with 'E'
e_majors = df[df['major'].str.startswith('E')]
print(e_majors)
```

## Conclusion

We've covered the basics of filtering in pandas, including:
- Single condition filtering
- Multiple condition filtering with logical operators
- Filtering on index values
- Using `.isin()` for multiple value matching
- String method filtering

These techniques form the foundation for data manipulation and analysis in pandas.