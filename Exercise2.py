# Question 1
# name = ["mohammad" , "ali" ,"ahmad" , "reza" , "keyvan"]
# longest_name = max(name,key=len)
# print(longest_name)


# Question 2
# a = [2,5,7]
# b = [3,6,4]

# if sum(a)>= sum(b):
#     result = a[::-1]
# else:
#     result = b[::-1]

# print(result)

# Question 3
# numbers = [1,2,2]
# reversed_numbers = list(reversed(numbers))

# if numbers == reversed_numbers:
#     print("palindrome")
# else:
#     print("not-palindrome")


# Question 4 - Way 1
# grades = [18, 14, 19, 17, 20, 13]
# biggest_number = max(grades)
# smallest_number = min(grades)

# grades.remove(biggest_number)
# grades.remove(smallest_number)

# average = sum(grades)/len(grades)

# print(average)

# Question4-Way 2
# grades = [18, 14, 19, 17, 20, 13]

# grades.remove(max(grades))

# grades.remove(min(grades))

# avg = (sum(grades))/len(grades)

# print(avg)

# Question 5 - Way 1

# ch = input("please enter character: ").lower()

# if ch=="a" or ch=="e" or ch=="o" or ch=="u" or ch=="i":
#     print("vowel sound")
# else:
#     print("not vowel sound")

# Question 5 - Way 2
# ch = input("please enter character: ").lower()
# vowel_sounds = ["a","e","i","o","u"]
# if ch in vowel_sounds:
#     print("vowel sound")
# else:
#     print("not-vowel sound")


# Question 5 - Way 3
# ch = input("please enter character: ").lower()
# vowel_sounds = "aeiou"
# if ch in vowel_sounds:
#     print("vowel sound")
# else:
#     print("not-vowel sound")

# Question6 - Way 1
# allowed_names=["amir","ali","ahmad","reza"]

# name = input("please enter name: ")
# card_status = input("do you have card?y/n ")
# password = input("please enter password: ")

# if name in allowed_names and card_status=="y" and (password=="temp" or password=="guest"):
#     print("welcome")
# else:
#     print("goodbye")

# Question6 - Way 2
# allowed_names=["amir","ali","ahmad","reza"]
# aloowed_pass = ["guest","temp"]

# name = input("please enter name: ")
# card_status = input("do you have card?y/n ")
# password = input("please enter password: ")

# valid_name = name in allowed_names
# valid_card = card_status=="y"
# valid_pass = password in aloowed_pass

# if valid_name and valid_card and valid_pass:
#     print("welcome")
# else:
#     print("goodbye")


# Question 7
# average = float(input("please enter average: "))
# lesson = input("please enter lesson: ")

# if average>18 and (lesson=="Medicine" or lesson=="Engineering"):
#     print("professional")
# elif average>16 and lesson=="Literature":
#     print("cultural")
# else:
#     print("Free")


# Question 8

blocked_users =["reza","ahmad","akbar"]

email = input("enter your email:")
password = input("enter your password:")
username = input("enter your username")

if "@" in email and len(password)>=6  and username not in blocked_users:
    print("successful")
else:
    if "@" not in email :
        print("unsuccessful ,it doesnt have @")
    if len(password)<6:
        print("unsuccessful , it must contain at least six character")
    if username in blocked_users :
        print ("unsuccessful , it shouldnt be in blocked users")

