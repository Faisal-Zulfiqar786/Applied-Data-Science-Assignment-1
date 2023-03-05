# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:35:42 2023

@author: raofa
"""
# Importing Pandas Library
import pandas as pd
# Importing matplotlib library for plotting
import matplotlib.pyplot as plt

#                                        Line Plot Program

# Read the CSV file into a pandas DataFrame
output = pd.read_csv('Line Plot.csv')
print(output)
# Extracting the values from column Country
Country= output['Country']
plt.figure()
# Using the matplotlib library's plot() function to create a line plot. 
# The plot will have output["Year"] as the x-axis values and output["Australia(US $)"] as the y-axis values.
plt.plot(output["Year"], output["Australia(US $)"], label="Australia(US $)")
plt.plot(output["Year"], output["Canada(US $)"], label="Canada(US $)")
plt.plot(output["Year"], output["Germany(US $)"], label="Germany(US $)")
plt.plot(output["Year"], output["United Kingdom(US $)"], label="United Kingdom(US $)")
plt.plot(output["Year"], output["UnitedStates(US $)"], label="UnitedStates(US $)")
# Using the matplotlib library's legend() function to add a legend to a plot also added fontsize and bbox_to_anchor to take more precise control on country variable values
plt.legend(Country, title="Countries", loc="lower left", fontsize=8, bbox_to_anchor=(-0.4, -0.15))

# Labeling the x-axis by using matplotlib libraray
plt.xlabel("Years")
# Labeling the y-axis by using matplotlib libraray
plt.ylabel("Annual Wages")
# Using matplot library for title the graph
plt.title("Annual wages of Different Countries ")
# Show the plot
plt.show()





#                                        Bar Plot Program


# Read the CSV file into a pandas DataFrame
data = pd.read_csv('GDP of Pak.csv')

# Extract the columns you want to use for the plot
x_column = 'Year'
y_column = 'GDP'
x = data[x_column]
y = data[y_column]

# Create the bar plot
plt.bar(x,y)

# Customize the plot by using matplotlib library for title, x-axis label and y-axis label
plt.title('GDP of Pakistan (2015-2021)')
plt.xlabel('Years')
plt.ylabel('GDP Per Annum')
# Using matplot library to add a legend to a plot
plt.legend()

# Show the plot
plt.show()


#                                        Pie Plot Program


# Read the CSV file into a pandas DataFrame
output = pd.read_csv('Pie chart.csv')
# Replaces comma and convert them into float
output['Budget'] = output['Budget'].str.replace(',', '.').astype(float)
# Extract labels and values from data
labels = output['Departments']
values = output['Budget']

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Total Departmental Expenditure Limits, 2021-22 (£millions)')
# Add legend
ax.legend(labels, title="Labels", loc="lower left", fontsize=7, bbox_to_anchor=(-0.4, -0.1))

# Show the plot
plt.show()





