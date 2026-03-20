# import mysql.connector

# import random

# def database_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="invoice_db"
#     )

# def display_invoice(customer_id):
#     connection = database_connection()
#     cursor=connection.cursor()
#     cursor.execute("SELECT * FROM customers WHERE id=%s",(customer_id))
#     customer=cursor.fetchone()
#     if not customer:
#         print("Invoice not found")
#         connection.close()
#         return
    
#     print("\n--------Invoice--------")
#     print("Invoice Number:",customer["invoice_number"])
#     print("Customer Name:", customer["customer_name"])
#     print("Mobile:",customer["mobile"])
#     print("Grand Total:",customer["grand_total"])
#     print("------------------")
#     print("--items--")
#     cursor.execute("SELECT * FROM invoice_items WHERE customer_id=%s",(customer_id))
#     items=cursor.fetchall()

#     for item in items:
#          print(f"{item['product_name']} | {item['product_price']} | {item['product_quantity']} | {item['item_total']}")
#     print("========================\n")
#     connection.close()

# def recalculate_total(customer_id):
#     connection =database_connection()
#     cursor=connection.cursor()
#     cursor.execute("SELECT SUM(item_total) as total FROM invoice_items WHERE customer_id=%s", (customer_id,))
#     total = cursor.fetchone()["total"] or 0
#     cursor.execute("UPDATE customers SET grand_total=%s WHERE id=%s", (total, customer_id))
#     connection.commit()
#     connection.close()

# def create_invoice():
#     invoice_number=random.randint(1000,9999)
#     name=input("Enter customer name:")
#     mobile=input("Enter mobile Number:")
#     while not mobile.isdigit() or len(mobile) != 10:
#         print("Enter a valid 10-digit mobile number")
#         mobile = input("Enter Mobile Number: ")

#     connection=database_connection()
#     cursor=connection.cursor()
#     cursor.execute(
#         "INSERT INTO customers(invoice_number,customer_name,mobile,grand_totak) VALUES (%s,%s,%s,%s)",
#         (invoice_number,name,mobile,0)
#     )
#     customer_id=cursor.lastrowid
#     connection.commit()

#     while True:
#         product_name=input("Enter Product Name: ")
#         price=float(input("Enter product Price: "))
#         quantity =int(input("enter product Quantity:"))
#         total=price*quantity

        
#         cursor.execute(
#             "INSERT INTO invoice_items (customer_id, product_name, product_price, product_quantity, item_total) VALUES (%s,%s,%s,%s,%s)",
#             (customer_id, product_name, price, quantity, total)
#         )
#         connection.commit()
#         recalculate_total(customer_id)

#         connection.commit()
#         recalculate_total(customer_id)

#         print("\n1. Add another item")
#         print("2. Finish Invoice")
#         choice = input("Enter choice: ")
#         if choice == '2':
#             break

#     connection.close()
#     display_invoice(customer_id)
#     print("Invoice created successfully!")

# def search_invoice():
#     invoice_no=input("Enter Invoice Number")
#     connection=database_connection()
#     cursor=connection.cursor()
#     cursor.execute("SELECT id FROM customers WHERE invoice_number=%s",(invoice_no))
#     customer=cursor.fetchone()
#     connection.close()
#     if customer:
#         display_invoice(customer["id"])
#     else:
#         print("Invoice not found!")


# def delete_invoice():
#     invoice_no=input("Enter Invoice number to Delete: ")
#     connection=database_connection()
#     cursor=connection.cursor()
#     cursor.execute("SELECT id FROM customer WHERE invoice_number=%s",(invoice_no,))
#     customer=cursor.fetchone()
#     if not customer:
#         print("Invoice not found")
#         connection.close()
#         return
#     delete_items=input("are you sure? y/n:")
#     if delete_items.lower()=="y":
#         cursor.execute("DELETE FROM customers WHERE inoives_number=%s",(invoice_no))
#         connection.commit()
#         print(" invoive delete!!")

#     else:
#         print("canceled!!")
#     connection.close()

# def update_invoice():
#     invoice_no = input("Enter Invoice Number to Update Items: ")
#     connection = database_connection()
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM customers WHERE invoice_number=%s", (invoice_no,))
#     customer = cursor.fetchone()

#     if not customer:
#         print("Invoice not found!")
#         connection.close()
#         return

#     customer_id = customer["id"]

#     while True:
#         pname = input("Enter product name to update: ")

#         # 🔹 Pehle check karo item exist karta hai ya nahi
#         cursor.execute(
#             "SELECT * FROM invoice_items WHERE customer_id=%s AND product_name=%s",
#             (customer_id, pname)
#         )
#         item = cursor.fetchone()

#         if item:
#             break   # Agar item mil gaya to loop se bahar
#         else:
#             print("Invalid item name! Please enter correct product name.")

#     # 🔹 Update values lo
#     new_price = float(input("New price: "))
#     new_qty = int(input("New quantity: "))
#     new_total = new_price * new_qty

#     # 🔹 Update query
#     cursor.execute(
#         """UPDATE invoice_items 
#            SET product_price=%s, product_quantity=%s, item_total=%s 
#            WHERE customer_id=%s AND product_name=%s""",
#         (new_price, new_qty, new_total, customer_id, pname)
#     )

#     connection.commit()

#     recalculate_total(customer_id)

#     print("Item updated successfully.")
#     connection.close()

# # -------- MAIN MENU --------
# while True:
#     print("\n------- INVOICE SYSTEM -----")
#     print("1. Create Invoice")
#     print("2. Search Invoice")
#     print("3. Update Invoice Items")
#     print("4. Delete Invoice")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == '1':
#        create_invoice()
#     elif choice == '2':
#         search_invoice()
#     elif choice == '3':
#         update_invoice()
#     elif choice == '4':
#         delete_invoice()
#     elif choice == '5':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice!")

import mysql.connector
import random

# -------- DATABASE CONNECTION --------
def database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="invoice_db"
    )

# -------- DISPLAY INVOICE --------
def display_invoice(customer_id):
    connection = database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers WHERE id=%s", (customer_id,))
    customer = cursor.fetchone()

    if not customer:
        print("Invoice not found")
        connection.close()
        return

    print("\n---------- Invoice ----------")
    print("Invoice Number:", customer["invoice_number"])
    print("Customer Name:", customer["customer_name"])
    print("Mobile:", customer["mobile"])
    # print("Grand Total:", customer["grand_total"])
    print("----------------------")
    print("Grand Total:", customer["grand_total"])
    print("-- Items --")

    cursor.execute("SELECT * FROM invoice_items WHERE customer_id=%s", (customer_id,))
    items = cursor.fetchall()

    for item in items:
        print(f"{item['product_name']} | {item['product_price']} | {item['product_quantity']} | {item['item_total']}")

    print("========================\n")
    connection.close()


# -------- RECALCULATE TOTAL --------
def recalculate_total(customer_id):
    connection = database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT SUM(item_total) as total FROM invoice_items WHERE customer_id=%s", (customer_id,))
    result = cursor.fetchone()
    total = result["total"] if result["total"] else 0

    cursor.execute("UPDATE customers SET grand_total=%s WHERE id=%s", (total, customer_id))
    connection.commit()
    connection.close()


# -------- CREATE INVOICE --------
def create_invoice():
    invoice_number = random.randint(1000, 9999)
    name = input("Enter customer name: ")
    mobile = input("Enter mobile number: ")

    while not mobile.isdigit() or len(mobile) != 10:
        print("Enter a valid 10-digit mobile number")
        mobile = input("Enter Mobile Number: ")

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO customers (invoice_number, customer_name, mobile, grand_total) VALUES (%s,%s,%s,%s)",
        (invoice_number, name, mobile, 0)
    )

    customer_id = cursor.lastrowid
    connection.commit()

    while True:
        product_name = input("Enter Product Name: ")
        price = float(input("Enter product Price: "))
        quantity = int(input("Enter product Quantity: "))
        total = price * quantity

        cursor.execute(
            "INSERT INTO invoice_items (customer_id, product_name, product_price, product_quantity, item_total) VALUES (%s,%s,%s,%s,%s)",
            (customer_id, product_name, price, quantity, total)
        )

        connection.commit()
        recalculate_total(customer_id)

        while True:
            more = input("Add more products? (y/n): ").lower()

            if more == 'y':
                break  
            elif more == 'n':
                connection.close()
                display_invoice(customer_id)
                print("Invoice created successfully!")
                return
            else:
                print("Please enter only y or n")




# -------- SEARCH INVOICE --------
def search_invoice():
    invoice_no = input("Enter Invoice Number: ")

    connection = database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()
    connection.close()

    if customer:
        display_invoice(customer["id"])
    else:
        print("Invoice not found!")


# -------- DELETE INVOICE --------
def delete_invoice():
    invoice_no = input("Enter Invoice number to Delete: ")

    connection = database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()

    if not customer:
        print("Invoice not found")
        connection.close()
        return

    confirm = input("Are you sure? (y/n): ")

    if confirm.lower() == "y":
        cursor.execute("DELETE FROM invoice_items WHERE customer_id=%s", (customer["id"],))
        cursor.execute("DELETE FROM customers WHERE id=%s", (customer["id"],))
        connection.commit()
        print("Invoice deleted successfully!")
    else:
        print("Cancelled!")

    connection.close()


# -------- UPDATE INVOICE --------
def update_invoice():
    invoice_no = input("Enter Invoice Number to Update Items: ")

    connection = database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers WHERE invoice_number=%s", (invoice_no,))
    customer = cursor.fetchone()

    if not customer:
        print("Invoice not found!")
        connection.close()
        return

    customer_id = customer["id"]

    while True:
        pname = input("Enter product name to update: ")

        cursor.execute(
            "SELECT * FROM invoice_items WHERE customer_id=%s AND product_name=%s",
            (customer_id, pname)
        )
        item = cursor.fetchone()

        if item:
            break
        else:
            print("Invalid item name! Try again.")

    new_price = float(input("New price: "))
    new_qty = int(input("New quantity: "))
    new_total = new_price * new_qty

    cursor.execute(
        """UPDATE invoice_items 
           SET product_price=%s, product_quantity=%s, item_total=%s 
           WHERE customer_id=%s AND product_name=%s""",
        (new_price, new_qty, new_total, customer_id, pname)
    )

    connection.commit()
    recalculate_total(customer_id)

    print("Item updated successfully.")
    connection.close()


# -------- MAIN MENU --------
while True:
    print("\n------- INVOICE SYSTEM -----")
    print("1. Create Invoice")
    print("2. Search Invoice")
    print("3. Update Invoice Items")
    print("4. Delete Invoice")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_invoice()
    elif choice == '2':
        search_invoice()
    elif choice == '3':
        update_invoice()
    elif choice == '4':
        delete_invoice()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
