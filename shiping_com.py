# user_area = "Mirpur"

# total_purchase_price = 1000

# if user_area in ["Mirpur","Farmgate","Dhanmondi"]:
#     if total_purchase_price >= 600:
#         print("shipping is free.")
#     elif total_purchase_price >= 300 and total_purchase_price < 600:
#         print("shipping price is 80")
#     else:
#         print("shipping is 150.")

# elif user_area in ["Mohakhali","Gulshan","badda"]:

# else:
#     print("shipping currently not available")


user_area = "Mohakhali", "Gulshan"

total_purchase_price = 800

if user_area in ["Mohakhali","Gulshan"]:
    if total_purchase_price >= 800:
        print("shipping is free.")
    elif total_purchase_price >= 500 and total_purchase_price < 800:
        print("shipping price is 100")
        
elif user_area in ["Mohakhali","Gulshan"]:
        print("shipping is 200.")
else:
    print("shipping currently not available")     
