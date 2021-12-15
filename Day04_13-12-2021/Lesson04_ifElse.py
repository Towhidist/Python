#User Login

u=input("Enter user name :")
p=input("Enter password :")

# if u.upper()=='Salam'.upper():
#     if p=="123":
#         print(f'Welcome Mr.{u}')
#     else:
#         print('invalid password !!!')
# else:
#     print('Sorry invalid user !!!')

if u.upper()=='Admin'.upper() and p=='123':
    print(f'Welcome Mr.{u}')
elif u.upper() != 'Admin'.upper() and p=='123':
    print('Invalid user name')
elif u.upper() == 'Admin'.upper() and p!='123':
    print('Invalid Password')
else:
    print('Both are invalid')