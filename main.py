#!/usr/bin/env python
# coding: utf-8

# In[1]:


import admin
from user import User

value = User(str, str, str, str, str)

ch = int(input("Choose one/n1.Admin/n2.User/n0.Exit"))
if ch == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if admin.admin_keys[Username] == Password:
        print("***** successfully logged inn*****")
        flag = True
        while flag:
            adm_choice = int(input("Choose any one\n1.ADD NEW FOOD\n2.EDIT FOOD LIST\n3.SHOW MENU\n4.REMOVE FOOD ITEM\n5.EXIT"))
            if adm_choice == 1:
                admin.add_new_item()
            elif adm_choice == 2:
                admin.edit_menu()
            elif adm_choice == 3:
                admin.show_menu()
            elif adm_choice == 4:
                admin.remove_food_item()
            elif adm_choice == 5:
                print(f"Your Exit from admin panel")
                flag = False
            else:
                print("please select valid option")
    else:
        print("wrong credentials! enter valid Credentials")
elif ch == 2:
    print("Here is the user panel")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        flag1 = True
        while flag1:
            choice = int(input(f"{username}, Enter the option\n1.Place new order\n2.Update Profile\n3.Order history\n4.See profile\n5.Exit"))
            if choice == 1:
                value.place_order()
            elif choice == 2:
                value.update_profile()
            elif choice == 3:
                print(f"Here is your order history, {username}")
                print(value.order_history)
            elif choice == 4:
                value.see_profile()
            elif choice == 5:
                flag1= False
                print("Successfully looged out")
            else:
                print("Invalid option")
    else:
        print("wrong credentials!")
else:
    print("Invalid option")


# In[ ]:




