try:
    age = int(input('age:'))
    income = 2000
    risk = income / age
    print(age)
except ValueError:
    print('invalid value')

except ZeroDivisionError:
    print("enter positive non-zero numbers")

