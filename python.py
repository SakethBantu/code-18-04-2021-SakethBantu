import json
     
def bmi(weight, height):
    return  (weight/(height/100)**2)

def category(BMI):
    if BMI <=18.4:
        return "Underweight"

    elif 18.5<= BMI <=24.9:
        return "Normal Weight"

    elif 25<= BMI <= 29.9:
        return "Overweight"
    
    elif 30 <= BMI <= 34.9:
        return "Moderately Obese"

    elif 35 <= BMI <= 39.9:
        return "Severely Obese"

    else:
        return "Very Severly Obese"

def  healthrisk(category):
    if category == "Underweight":
        return "Malnutrition Risk"

    elif category == "Normal Weight":
        return "Low Risk"

    elif category == "Overweight":
        return "Enhanced Risk"
    
    elif category == "Moderately Obese":
        return "Medium Risk"
    
    elif category == "Severely Obese":
        return "High Risk"

    elif category == "Very Severely Obese":
        return "Very High Risk"

with open('bmi_input.json') as p:
    data = json.load(p)

for n in data['people']:
    
    n["BMI"] = bmi(n['WeightKg'],n['HeightCm'])
    n["category"] = category(n["BMI"])
    n["healthrisk"] = healthrisk(n["category"])          


def taskII(overweightcount):
    j = 0
    for m in overweightcount:
        
        if(m["category"]=="Overweight"):
            j =+ 1
        
    return j

print(data)    
print("Number of Overweight people: {}".format(taskII(data['people'])))

with open('bmi_output.txt', 'w+') as output:
    json.dump(data, output)
    
