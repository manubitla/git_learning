import numpy
import pandas as pd
from datetime import date, datetime

# 10. Write a Pandas program to convert Series of lists to one Series.
series_lists = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['yellow']])
print(series_lists.apply(pd.Series).stack().reset_index(drop=True))

data = pd.DataFrame({'EmployeeName': ['Callen Dunkley', 'Sarah Rayner', 'Jeanette Sloan', 'Kaycee Acosta',
                                      'Henri Conroy', 'Emma Peralta', 'Martin Butt', 'Alex Jensen', 'Kim Howarth',
                                      'Jane Burnett'],
                     'Department': ['Accounting', 'Engineering', 'Engineering', 'HR', 'HR', 'HR', 'Data Science',
                                    'Data Science', 'Accounting', 'Data Science'],
                     'HireDate': [2010, 2018, 2012, 2014, 2014, 2018, 2020, 2018, 2020, 2012],
                     'Sex': ['M', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'F'],
                     'Birthdate': ['04/09/1982', '14/04/1981', '06/05/1997', '08/01/1986', '10/10/1988', '12/11/1992',
                                   '10/04/1991', '16/07/1995', '08/10/1992', '11/10/1979'],
                     'Weight': [78, 80, 66, 67, 90, 57, 115, 87, 95, 57],
                     'Height': [176, 160, 169, 157, 185, 164, 195, 180, 174, 165],
                     'Kids': [2, 1, 0, 1, 1, 0, 2, 0, 3, 1]
                     })
#print(data)


# Scenario 1:
# Let's assume that the HR team wants to send an invitation email that starts with a friendly greeting '
# to all the employees (e.g., Hey, Sarah!). They asked you to create two columns for storing the
# employees(' first and last names separately, making referring to the employees’ first names easy. '
# 'To do so, we can use a lambda function that splits a string into a list after breaking it by the '
# specified separator; the default separator character of the split() method is any white space.


# let's create two more columns in the data DataFrame and place firstname and lastname separately

data['First Name'] = data['EmployeeName'].apply(lambda x: x.split()[0])
data['Last Name'] = data['EmployeeName'].apply(lambda x: x.split()[1])
print(data.to_string())


# Scenario 2
#
# Now, let's assume that the HR team wants to know every employee's age and the average age of
# the employees because they want to determine if an employee('s age influences job satisfaction '
# and work engagement.)
# To get the job done, the first step is to define a function that gets an employee('s date of birth '
# and returns their age:)


def age_calculator(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
    print(birthdate)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


data['Emp Age'] = data['Birthdate'].apply(age_calculator)
print(data.to_string())


# Scenario 3
# The HR manager of the company is exploring options for healthcare coverage for all employees.
# Potential providers require information about the employees.
# Since the DataFrame contains the weight and height of each employee, let’s assume the HR manager
# asked you to provide a Body Mass Index (BMI) for every employee so she can get quotes from
# potential healthcare providers.
#
# To do the task, first, we need to define a function that calculates the Body Mass Index (BMI). T
# he formula for the BMI is weight in kilograms divided by height in meters squared.
# Because the employees’ heights are measured in centimeters, we need to divide the heights by 100
# to obtain the heights in meters. Let’s implement the function:


def bmi_calculator(weight, height):
    return numpy.round(weight / (height / 100) ** 2, 2)


data['BMI'] = data.apply(lambda x: bmi_calculator(x['Weight'], x['Height']), axis=1)
print(data.to_string())


# Scenario 4:
# A BMI of less than 18.5 is Group One, between 18.5 and 24.9 is Group Two, between 25 and 29.9 is
# Group Three, and over 30 is Group Four. To implement the solution, we will define a function
# that returns the various BMI indicators, then apply it on the BMI column of the DataFrame to see
# each employee falls into which category:


def bmi_indicator(bmi):
    if bmi <= 18.5:
        return "Group One"
    elif 18.6 <= bmi <= 24.9:
        return "Group Two"
    elif 25 <= bmi <= 29.9:
        return "Group Three"
    elif bmi >= 30:
        return "Group Four"


data['BMI_Indicator'] = data['BMI'].apply(bmi_indicator)

print(data.to_string())

# Scenario 4
# Let’s assume the new year is around the corner and the company management has announced
# that those employees who have more than ten years of experience will get an extra bonus.
# The HR manager wants to know who is qualified to get the bonus.
#
# To prepare the requested information, you need to apply the following lambda function
# on the HireDate column, which returns True if the difference between the current year and
# the hire year is greater than or equal to ten years otherwise False.
exp_10 = data['HireDate'].apply(lambda x: date.today().year - x > 10)
print(exp_10)
print(data[exp_10].to_string())

# Scenario 5
# Let’s assume that tomorrow is Mother’s Day, and the company has planned a Mother’s Day gift
# for all its female employees who have children. The HR team asked you to prepare a list of the
# employees who are eligible for the gift. To do the task, we need to write a simple lambda function
# that considers the Sex and Kids columns to provide the desired result, as follows:
print(data.columns.tolist())


def mothers_gift(gender, kids):
    if gender == 'F' and kids > 0:
        return True
    else:
        return False


data['mothers_day_gift'] = data.apply(lambda x: mothers_gift(x['Sex'], x['Kids']), axis=1)
print(data.to_string())
