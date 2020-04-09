import string
import random

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
email = input("Enter your Eamil Address: ")

letters = string.ascii_lowercase

full_name = f_name + " " + l_name;
a = f_name[0:2]
b = (l_name[(len(l_name)-2):(len(l_name)+1)]);
password = 0
password = a + b + randomString(5);

user_details = {
    "firstname" : f_name,
    "Last name" : l_name,
    "Email" : email,
    "Password" : password
}

print("This is your Password", password)
print("is Password Okay")
choice = input("Yes or No : ")

if choice == "yes":
    print(user_details)

else:
    password2 =input("Input  your preferd 9 digit password ")
    while len(password2) < 7 :
        password2 = input("Input  your preferd 9 digit password ")
        user_details["Password"] = password2

print(user_details)

print("your details: ")
for x in user_details:
    print(user_details[x])
