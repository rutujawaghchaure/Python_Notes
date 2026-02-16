# import random
# num = random.randint(1000, 9999)
# name = input("Enter Your Name: ")

# Mobilenumber = input("Enter Number: ")
# while not Mobilenumber.isdigit() or len(Mobilenumber) != 10 or Mobilenumber[0] not in ['7','8','9']:
#     print("Enter a valid 10-digit mobile number")
#     Mobilenumber = input("Enter Number: ")

# products = []
# grand_total = 0

# while True:
#     productname = input("Enter Product Name: ")

#     productprice = input("Enter Product Price: ")
#     while not productprice.isdigit():
#         print("Enter a valid number")
#         productprice = input("Enter Product Price: ")

#     productquantiti = input("Enter Product Quantity: ")
#     while not productquantiti.isdigit():
#         print("Enter a valid number")
#         productquantiti = input("Enter Product Quantity: ")

#     item_total = int(productprice) * int(productquantiti)
#     grand_total += item_total



#     products.append({
#         "Product Name": productname,
#         "Product Price": productprice,
#         "Product Quantity": productquantiti,
#         "Item Total": item_total
#     })

#     while True:
#         print("1. Add  item")
#         print("2. Update item")
#         print("3. Delete item")
#         print("4. Exit")
#         choice = input("Enter Your choice: ")

#         if choice == '1':
#             break  
#         elif choice == '2':
#             update_name=input("enter product name to update : ")
#             for item in products:

#                 productname=input("Enter the product name:")
#                 productprice = input("Enter Product Price: ")
#                 while not productprice.isdigit():
#                     print("Enter a valid number")
#                 productprice = input("Enter Product Price: ")
            
#             break
#         elif choice == '3':
#             delete_name = input("enter product name to delete: ")
            

#             for item in products:
#                 if item["product Name"] == delete_name:
#                     products.remove(item)
                
#                 print("Item deleted successfully!")
#                 break

        
#             print("Product not found!")
#         elif choice == '4' :
#             break 
#         else:
#             print("Invalid choice. Please enter 1,2,3 or 4.")

#     if choice == '4':
#         break  

# print("\n------------------Invoice Items----------------------")
# print("Customer Name:", name)
# print("Invoice Number:", num)
# print("Phone Number:", Mobilenumber)
# print("Product Name\tProduct Price\tProduct Quantity\tItem Total")
# for item in products:
#     print(f"{item['Product Name']}\t\t{item['Product Price']}\t\t{item['Product Quantity']}\t\t\t{item['Item Total']}")
# print("\n------------------------------------------------------")
# print("Grand Total:", grand_total)
# print("--------------------------------------------------------")



import random

num = random.randint(1000, 9999)
name = input("Enter Your Name: ")

Mobilenumber = input("Enter Number: ")
while not Mobilenumber.isdigit() or len(Mobilenumber) != 10 or Mobilenumber[0] not in ['7','8','9']:
    print("Enter a valid 10-digit mobile number")
    Mobilenumber = input("Enter Number: ")

products = []

while True:
    print("\n1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    
    if choice == '1':
        productname = input("Enter Product Name: ")

        productprice = input("Enter Product Price: ")
        while not productprice.isdigit():
            print("Enter a valid number")
            productprice = input("Enter Product Price: ")

        productquantity = input("Enter Product Quantity: ")
        while not productquantity.isdigit():
            print("Enter a valid number")
            productquantity = input("Enter Product Quantity: ")

        item_total = int(productprice) * int(productquantity)

        products.append({
            "Product Name": productname,
            "Product Price": int(productprice),
            "Product Quantity": int(productquantity),
            "Item Total": item_total
        })

        print("Item added successfully!")

    
    elif choice == '2':
        update_name = input("Enter product name to update: ")
        found = False

        for item in products:
            if item["Product Name"] == update_name:
                found = True

                new_price = input("Enter New Price: ")
                while not new_price.isdigit():
                    print("Enter valid number")
                    new_price = input("Enter New Price: ")

                new_quantity = input("Enter New Quantity: ")
                while not new_quantity.isdigit():
                    print("Enter valid number")
                    new_quantity = input("Enter New Quantity: ")

                item["Product Price"] = int(new_price)
                item["Product Quantity"] = int(new_quantity)
                item["Item Total"] = int(new_price) * int(new_quantity)

                print("Item updated successfully!")
                break

        if not found:
            print("Product not found!")

    
    elif choice == '3':
        delete_name = input("Enter product name to delete: ")
        found = False

        for item in products:
            if item["Product Name"] == delete_name:
                products.remove(item)
                found = True
                print("Item deleted successfully!")
                break

        if not found:
            print("Product not found!")

    
    elif choice == '4':
        break

    else:
        print("Invalid choice!")


grand_total = 0
for item in products:
    grand_total += item["Item Total"]


print("\n------------------Invoice----------------------")
print("Customer Name:", name)
print("Invoice Number:", num)
print("Phone Number:", Mobilenumber)
print("------------------------------------------------")
print("Product Name\tPrice\tQuantity\tTotal")

for item in products:
    print(f"{item['Product Name']}\t\t{item['Product Price']}\t{item['Product Quantity']}\t\t{item['Item Total']}")

print("------------------------------------------------")
print("Grand Total:", grand_total)
print("------------------------------------------------")
