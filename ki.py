import sql2

weight = sql2.ex.weight
height = sql2.ex.height
age = sql2.ex.age
gender=sql2.ex.gender
activity=sql2.ex.activity
print("username:",sql2.ex.username)
print("preference:",sql2.ex.preference)

if gender == "Male" :
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    print("BMR of male", BMR)
else :
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    print("BMR of female", BMR)

if activity == "Light exercise":
    print("light exercise")
    dkc = BMR * 1.375
elif activity == "Little to no exercise":
    print("little to no  exercise")
    dkc = BMR * 1.2
elif activity == "Moderate exercise":
    print("moderate exercise")
    dkc = BMR * 1.55

elif activity == "Heavy exercise":
    dkc = BMR * 1.725
    print("heavy exercise")

else:
    dkc = BMR * 1.9

print("dkc", dkc)

