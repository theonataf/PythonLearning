# num1= 2
# num2 = 3
#
# def add(number1, number2):
#     adding = number1+ number2
#     return adding
#
# print(add(number1=num1, number2=num2))




import json

f = open('network.json', 'r')
network = json.load(f)
users = network['users']
f.close()

def create_new_user():
    username = input('username')

    new_user = {
        'username': username,
        'password': password,
        "email": email,
        "message_received": [],
        "message_sent": []
    }
    users.append(new_user)

    return new_user

def log_in():
    username = input('What is your username ?')
    password = input('What is your password ?')

    for user in users:
        if user['username'] == username:
            for i in range(3):
                if user['password'] == password:
                    print('you are logged in')
                    return user
                else:
                    password = input('Password wrong please enter it again ?')
    print(" We didn't find any user matching those credentials do you want to create one ?")
    answer = int(input("\n\t(1)Yes\n\t(2)No"))
    if answer == 1:
        create_new_user()
    else:
        return 0


print(log_in())




