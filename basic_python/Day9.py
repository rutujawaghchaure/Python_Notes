import mysql.connector

# ---------- DATABASE CONNECTION ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_invoice"
)

cursor = conn.cursor()

# ---------- SAVE INVOICE ----------
def save_invoice(products, name, phone, grand_total):

    # Check if customer exists
    cursor.execute("SELECT customer_id FROM customers WHERE phone = %s", (phone,))
    customer = cursor.fetchone()

    if customer:
        customer_id = customer[0]
    else:
        cursor.execute(
            "INSERT INTO customers (customer_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        customer_id = cursor.lastrowid

    # Insert invoice
    cursor.execute(
        "INSERT INTO invoices (customer_id, grand_total) VALUES (%s, %s)",
        (customer_id, grand_total)
    )
    invoice_id = cursor.lastrowid

    # Insert invoice items
    for item in products:
        cursor.execute("""
            INSERT INTO invoice_items
            (invoice_id, product_name, product_price, quantity, item_total)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            invoice_id,
            item["Product Name"],
            item["Product Price"],
            item["Product Quantity"],
            item["Item Total"]
        ))

    conn.commit()
    print(f"\n Invoice Saved Successfully! Invoice ID: {invoice_id}")


def display_invoice_from_db(invoice_id):

    query = """
    SELECT c.customer_name, c.phone,
           i.invoice_id, i.invoice_date, i.grand_total,
           ii.product_name, ii.product_price,
           ii.quantity, ii.item_total
    FROM invoices i
    JOIN customers c ON i.customer_id = c.customer_id
    JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
    WHERE i.invoice_id = %s
    """

    cursor.execute(query, (invoice_id,))
    results = cursor.fetchall()

    if results:
        print("\n============= INVOICE =============")
        print(f"Invoice ID : {results[0][2]}")
        print(f"Date       : {results[0][3]}")
        print(f"Customer   : {results[0][0]}")
        print(f"Phone      : {results[0][1]}")
        print("-----------------------------------")
        print("Product\tPrice\tQty\tTotal")
        print("-----------------------------------")

        for row in results:
            print(f"{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}")

        print("-----------------------------------")
        print(f"Grand Total : {results[0][4]}")
        print("===================================\n")

    else:
        print("❌ Invoice Not Found!")

# ---------- SEARCH INVOICE ----------
def search_invoice(invoice_id):

    query = """
    SELECT c.customer_name, c.phone,
           i.invoice_id, i.invoice_date, i.grand_total,
           ii.product_name, ii.product_price,
           ii.quantity, ii.item_total
    FROM invoices i
    JOIN customers c ON i.customer_id = c.customer_id
    JOIN invoice_items ii ON i.invoice_id = ii.invoice_id
    WHERE i.invoice_id = %s
    """

    cursor.execute(query, (invoice_id,))
    results = cursor.fetchall()

    if results:
        print("\n========== INVOICE DETAILS ==========")
        for row in results:
            print(f"""
Customer Name : {row[0]}
Phone         : {row[1]}
Invoice ID    : {row[2]}
Date          : {row[3]}
Grand Total   : {row[4]}
Product       : {row[5]}
Price         : {row[6]}
Quantity      : {row[7]}
Item Total    : {row[8]}
----------------------------------------
""")
    else:
        print(" Invoice Not Found!")

# ---------- DELETE INVOICE ----------
def delete_invoice(invoice_id):

    cursor.execute("DELETE FROM invoice_items WHERE invoice_id = %s", (invoice_id,))
    cursor.execute("DELETE FROM invoices WHERE invoice_id = %s", (invoice_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(" Invoice Deleted Successfully!")
    else:
        print(" Invoice Not Found!")


# ---------- CREATE NEW INVOICE ----------
def create_invoice():

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")

    while not phone.isdigit() or len(phone) != 10:
        print("Enter valid 10-digit number")
        phone = input("Enter Phone Number: ")

    products = []
    grand_total = 0

    while True:
        productname = input("\nEnter Product Name: ")
        productprice = float(input("Enter Product Price: "))
        quantity = int(input("Enter Quantity: "))

        item_total = productprice * quantity
        grand_total += item_total

        products.append({
            "Product Name": productname,
            "Product Price": productprice,
            "Product Quantity": quantity,
            "Item Total": item_total
        })

        more = input("Add more products? (y/n): ")
        if more.lower() != 'y':
            break

    save_invoice(products, name, phone, grand_total)

# ---------- MAIN MENU ----------
while True:
    print("\n====== PROFESSIONAL BILLING SYSTEM ======")
    print("1. Create New Invoice")
    print("2. Search Invoice")
    print("3. Delete Invoice")
    # print("4. Update Invoice")
    print("5. Display Invoice")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_invoice()

    elif choice == '2':
        invoice_id = input("Enter Invoice ID: ")
        search_invoice(invoice_id)

    elif choice == '3':
        invoice_id = input("Enter Invoice ID to delete: ")
        delete_invoice(invoice_id)
    # elif choice =='4':
    #     invoice_id=input("Enter  inVoice id to update:")
    #     update_invoice(invoice_id)

    elif choice == '5':
        invoice_id = input("Enter Invoice ID to display: ")
        display_invoice_from_db(invoice_id)   
    

    elif choice == '6':
        break

    else:
        print("Invalid choice!")

# ---------- CLOSE CONNECTION ----------
cursor.close()
conn.close()

print("\n Program Ended Successfully!")