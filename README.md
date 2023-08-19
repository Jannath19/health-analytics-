# health-analytics-
Assignment primer for course 504/507 involving GitHub, Google Shell, and Python

# Health Analysis Project

This project contains a Python script (`health_analysis.py`) that demonstrates the usage of variables, functions, and data analysis using pandas and numpy.

## Variables Used

- **Number Variable:** I created the patient's age, which is 45.

- **String Variable:** I created the patient's name, which is Alex.

- **List Variable:** I created the patient's health conditions: diabetes, hypothyroidism, and arthritis.

- **Dictionary Variable:** I created the patient's health record, including the patient's name, age, health conditions, and current medications.

## Explanation of the Function

The function `measure_o2sat` assesses the oxygen saturation level of a patient based on two inputs: whether the individual has hypothyroidism and their oxygen saturation level. If the patient has hypothyroidism and their oxygen saturation level is below 94, the function advises "Put on oxygen respirator." If the patient has hypothyroidism and their oxygen saturation level is 95, the function suggests "Keep observation on o2sat." If the patient has hypothyroidism and their oxygen saturation level is neither of the above conditions, the function concludes "No need for oxygen respirator."

## Expected Output Based on Data

 No need for oxygen respirator
