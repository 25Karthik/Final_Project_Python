#!/usr/bin/env python
# coding: utf-8

# In[2]:


import admin

class User:
    info_login = {}

    def __init__(self, name, phone_no, email, address, password):
        self.name = name
        self.number = phone_no
        self.email = email
        self.address = address
        self.password = password
        User.info_login[self.name] = self.password
        self.profile = {}
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.info_login.get(username) == password:
            print(" successfully logged in.....")
            return True
        else:
            print("SORRY! Wrong Credentials")
            return False

    def see_profile(self):
        self.profile[self.name] = {
            "Full Name": self.name,
            "Phone Number": self.number,
            "E-Mail": self.email,
            "Address": self.address,
            "Password": self.password
        }
        return self.profile

    def update_profile(self):
        x = input("What you want to update in your profile..")
        y = input("And changes to the new one: ")
        self.profile[x] = y
        print("Your Profile is Updated")
        return self.profile

    def place_order(self):
        print(" Here is the menu for Order")
        print(admin.show_menu())
        print("Enter the food ID to order the food")
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            foodid = int(input("Enter the food id here: "))
            quan = int(input("Enter the quantity of the food: "))
            x = admin.menu[foodid]["Price"] * quan
            again= input("Are you still want to order this Enter YES or NO")
            if again == "YES":
                print(f'''Your food name is {admin.menu[foodid]["Food Name"]}''')
                print(f'''Price of your food is {admin.menu[foodid]["Price"]}''')
                print(f"quantity {quan}")
                print(f"It will costs you {x}INR in total")
                print("Your all set for the order")
                self.order_history[foodid] = {
                    "Food Name": admin.menu[foodid]["Food Name"],
                    "Price": admin.menu[foodid]["Price"],
                    "Quantity": quan
                }
                final_stock = admin.menu[foodid]["Stock"] - quan
                admin.menu[foodid]["Stock"] = final_stock
                print(" successfully placed")

            elif again== "NO":
                print("This Order is cancelled!!")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def see_profile(self):
        print(self.profile)
        
    def order_his(self):
        print(self.order_history)



karthik = User("karthik", "9945623593", "karthik.3268@gmail.com", "Mysuru,karnataka", "karthik$123")
jeevan=  User("jeevan", "98801500023", "jeevan3568@gmail.com", "Bangaluru,karnataka", "jeevan*123")


# In[ ]:




