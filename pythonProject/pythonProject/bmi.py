print("diese Programm rechent BMI")
wight_str= input("Bitte gebe dien Gewicht in kg ein:")
height_str= input ("Bitte gebe dien Köpergrosse im m in kg ein:")

weight = float(wight_str.replace(",","."))
height = float(height_str.replace(",","."))

BMI = weight / height ** 2
print("BMI: "+ str(round(BMI,1)))