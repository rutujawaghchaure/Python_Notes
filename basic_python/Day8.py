import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_info"
)


cursor = conn.cursor()
def display_invoice(products, grand_total, name, num, Mobilenumber):
    print("\n----------- INVOICE -----------")
    print("Customer Name:", name)
    print("Invoice Number:", num)
    print("Phone Number:", Mobilenumber)
    print("\nProduct\tPrice\tQty\tTotal")

    for item in products:
        print(f"{item['Product Name']}\t{item['Product Price']}\t{item['Product Quantity']}\t{item['Item Total']}")

    print("\nGrand Total:", grand_total)
    print("-------------------------------")

def save_to_mysql(products, name, phone):
    
    # 1️ Insert customer
    customer_sql = """
    INSERT INTO customers (customer_name, phone)
    VALUES (%s, %s)
    """
    cursor.execute(customer_sql, (name, phone))
    
    # Get inserted customer_id
    customer_id = cursor.lastrowid

    # 2️ Insert products linked with customer_id
    product_sql = """
    INSERT INTO products (product_name, product_price, customer_id)
    VALUES (%s, %s, %s)
    """

    for item in products:
        values = (
            item["Product Name"],
            item["Product Price"],
            customer_id
        )
        cursor.execute(product_sql, values)

    conn.commit()
    print("Customer and products saved successfully!")

# ---------- Main Program ----------
num = random.randint(1000, 9999)
name = input("Enter Your Name: ")

Mobilenumber = input("Enter Number: ")
while not Mobilenumber.isdigit() or len(Mobilenumber) != 10:
    print("Enter valid 10-digit number")
    Mobilenumber = input("Enter Number: ")

products = []
grand_total = 0

while True:
    productname = input("\nEnter Product Name: ")

    productprice = int(input("Enter Product Price: "))
    productquantity = int(input("Enter Product Quantity: "))

    item_total = productprice * productquantity
    grand_total += item_total

    products.append({
        "Product Name": productname,
        "Product Price": productprice,
        "Product Quantity": productquantity,
        "Item Total": item_total
    })

    print("\n1. Add More")
    print("2. Display Invoice") 
    print("5. Save AND Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        continue

    elif choice == '2':
        display_invoice(products, grand_total, name, num, Mobilenumber)

    elif choice == '3':
        break
    elif choice =='4':
        break


    elif choice == '5':
        save_to_mysql(products, name, Mobilenumber)
        
        break

    else:
        print("Invalid choice")

# Close connection
cursor.close()
conn.close()

print("Program Ended Successfully!")





