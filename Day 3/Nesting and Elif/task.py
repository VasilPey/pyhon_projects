weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi < 25 & int(bmi > 18):
    print("normal weight")
else:
    print("overweight")