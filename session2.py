# input

# name = input("please enter name: ")
# print(name)

# get a number --> show 5*number
# n = int(input("please enter n: "))
# print(n*5)

# operator ---> numbers
# string --> operator --> + *
# "amir" * 5
# "amir" + "reza"

# firstname = "amirhossein"
# print(firstname*5)

# lastname = "hajitabar"
# print(firstname+" "+lastname)

# LIST
# scores = [10,12,15,14,5]
# print(scores)
# print(type(scores))
# print(scores[2])

# cars = ["bmw","prado","dudge","mitsubishi","bmw"]

# cars[2] = "dodge"
# print(cars)

# cars.append("toyota")
# print(cars)

# cars.insert(1,"hyundai")
# print(cars)

# del cars[1]
# print(cars)

# deletedCar = cars.pop(1)
# print(f"car {deletedCar} sold!!")
# print(cars)

# cars.remove("bmw")
# print(cars)


# numbers = [10,12,16,18,8,6]

# numbers.sort(reverse=True)
# print(numbers)


# cars = ["bmw","prado","dudge","mitsubishi"]
# cars.sort()
# print(cars)

# sortedNumbers = sorted(numbers)
# print(sortedNumbers)
# print(numbers)

# numbers.reverse()
# print(numbers)


# reversedNumbers = reversed(numbers)
# print(list(reversedNumbers))
# print(numbers)

# print(numbers[::-1])

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# print(sum(numbers)/len(numbers))

# score = int(input("please enter score: "))
# if score>=10:
#     print("pass")
# else:
#     print("fail")

# a=5
# b=6

# if a==b:
#     print("equal")
# else:
#     print("not-equal")


# username = input("please enter username: ")
# password = input("please enter password: ")

# if username=="admin" and password=="admin":
#     print("login")
# else:
#     print("need signup")

n= int(input("please enter n: "))
if n>0:
    print("positive")
elif n==0:
    print("zero")
else:
    print("negative")
