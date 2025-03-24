#Taveon James
#10/4/2024
#project

print("Welcome To Shake Shack")
print("1.ShacKChicken... $5.25,\n2.ShackBeefBurger... $6.25,\n3.ShackTofuSandwich... $5.75")
user_sandwich = int(input("Enter a number: "))
total_cost = 0.0

order = ["", "", "", 0]
sandwich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3



if user_sandwich == 1:
    order[sandwich_index] = "ShackChicken"
    total_cost += 5.25
elif user_sandwich == 2:
    order[sandwich_index] = "ShackBeefBurger"
    total_cost += 6.25
elif user_sandwich == 3:
    order[sandwich_index] = "ShackTofuSandwich"
    total_cost += 5.75

print(f"\nTotal Spent So Far: {total_cost}")

user_bev = int(input("Enter 1 for yes for a bev, or 2 for no for no bev:"))

if user_bev == 1:
    user_bevy_size = int(input("What size is your bev?\n 1. Small ... $1.00\n 2. Medium ... $1.75\n 3. Large ... $2.25: "))
    print(f"Your bevy size is {user_bevy_size}")
    if user_bevy_size == 1:
        order[beverage_index] = "Small"
        total_cost += 1.00
    elif user_bevy_size == 2:
        order[beverage_index] = "Medium"
        total_cost += 1.75
    elif user_bevy_size == 3:
        order[beverage_index] = "Large"
        total_cost += 2.25
elif user_bev == 2:
    print("No bev chosen!")

print(f"\nTotal Spent So Far: {total_cost}")

user_fries = int(input("Enter 1 for yes for a fries, or 2 for no for no fries:"))

# taveom
if user_fries == 1:
    user_shackfries_size = int(input("What size is your fries?\n 1. Small ... $1.00\n 2. Medium ... $1.75\n 3. Large ... $2.25: "))
    print(f"Your shackfries size is {user_shackfries_size}")
    if user_shackfries_size == 1:
        order[fries_index] = "Small"
        user_megafries = int(input("would you like to mega size your fries 1. yes 2. no"))
        if user_megafries == 1:
            total_cost += 2.00
        elif user_megafries == 2:
            total_cost += 1.00
            order[fries_index] = "Medium"
        total_cost += 1.50
    elif user_shackfries_size == 3:
        order[fries_index] = "Large"
        total_cost += 2.00
elif user_fries == 2:
    print("No fries chosen!")



ketchup_packets = int(input("How many ketchup packets would you like? "))
total_cost += (ketchup_packets * 0.25)

order[ketchup_index] = ketchup_packets
if user_fries == 1 and user_bev == 1:
    total_cost -= 1