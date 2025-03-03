
typeofconversion = input("Select the type of conversion you want (length, weight, temp) : ")

if typeofconversion.lower() == "length":
    _length = float(input("Enter the length: "))
    unit=input("meter or foot ? (M or F): ")
    if unit.lower()=='m':
        _length = _length * 3.28
        print(f"The converted length is {round(_length,2)} ft.")
    elif unit.lower()=='f':
        _length = _length / 3.28
        print(f"The converted length is {round(_length,2)} m.")
    else:
        print("{unit} is not a valid conversion for length")
    
elif typeofconversion.lower() == "weight":
    _weight = float(input("Enter the weight: "))
    unit=input("Kilograms or Pound ? (K or L): ")
    if unit.lower()=='k':
        _weight = _weight * 2.20
        print(f"The converted weight is {round(_weight,2)} Lbs.")
        
    elif unit.lower()=='l':
        _weight = _weight / 2.20
        print(f"The converted weight is {round(_weight,2)} KG.")
    else:
        print("{unit} is not a valid conversion for weight")

elif typeofconversion.lower() == "temp":
    _temp = float(input("Enter the temperature: "))
    unit=input("Celsius or Fahrenhiet ? (C or F): ")
    if unit.lower()=='c':
        _temp = _temp * 1.8 +32
        print(f"The converted temperature is {round(_temp, 2)} F.")
    elif unit.lower()=='f':
        _temp = (_temp - 32) * 5/9
        print(f"The converted temperature is {round(_temp, 2)} C.")
        
    else:
        print("{unit} is not a valid conversion for temperature")

else:
    print("Invalid conversion type")
   
