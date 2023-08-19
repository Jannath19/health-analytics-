import pandas as pd
import numpy as np 

# Variables
patient_firstName = "Alex"
patient_age = 45
patient_healthconditions = ["diabetes", "hypothyroidism", "arthritis"]
patient_o2sat = 98

patient_information = {
    "patient_age": 45,
    "firstName": "Alex",
    "patient_pastInformation": {
        "current health conditions": ["diabetes", "hypothyroidism", "arthritis"],
        "current medications": {
            "diabetes": "insulin",
            "hypothyroidism": "levothyroxine",
            "arthritis": "ibuprofen"
        }
    }
}

# Function
def measure_o2sat(conditions, o2sat):
    if o2sat < 94 and "hypothyroidism" in conditions:
        return "Put on oxygen respirator"
    elif o2sat == 95 and "hypothyroidism" in conditions:
        return "Keep observation on o2sat"
    else:
        return "No need for oxygen respirator"

# Print functions
print("Patient First Name:", patient_firstName)
print("Patient Age:", patient_age)
print("Patient Health Conditions:", patient_healthconditions)
print("Patient Oxygen Saturation Level:", patient_o2sat)
print("Patient Medical Information Recorded:", patient_information)

# Example run with data
o2sat_result = measure_o2sat(patient_healthconditions, patient_o2sat)
print("Patient Oxygen Saturation Level:", patient_o2sat)
print("Oxygen Saturation Result:", o2sat_result)
