import random
key_value = {"Karthik": "karthik@321"}

menu = {1: {'Food Name': 'Chicken Kabbab', 'Food ID': 2, 'Price': 150, 'Discount': 0, 'Stock': 123}}

def edit_menu():
    food = int(input("Enter the food_id of the food which you want to edit: "))
    new_name= input("Enter the food name")
    new_price= int(input("Enter the price of food"))
    new_discount= int(input("Enter the discount of food"))
    new_stock= int(input("Enter the stock of the food"))
    menu[food]["Food Name"] = new_name
    menu[food]["Price"] = new_price
    menu[food]["Discount"] = new_discount
    menu[food]["Stock"] = new_stock
    print("*****Edited food item successfully*****")
    return menu


def add_new_item():
    food_name = input("Enter the foood name: ")
    food_id = random.randint(5,1000)
    price = int(input("Enter the price of the food: "))
    discount = int(input("Enter the discount of food: "))
    stock = int(input("Enter te stock value of food: "))
    menu[foodid] = {
        "Food Name": food_name,
        "Food ID": food_id,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    print(f"The {foodname} with {food_id} is successfully added")
    return menu


def show_menu():
    print("***** MENU OF THE RRR Hotel *****")
    for i in menu:
        print("Food Name: ",menu[i]["Food Name"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Food ID: ",menu[i]["Food ID"])

def remove_food_item():
    delete= int(input("Enter the food id which you want to exit"))
    menu.pop(delete)
    print("Removed food item successfully ")
    return menu

