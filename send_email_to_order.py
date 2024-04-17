import pyodbc
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Product:
    def __init__(self, uniq_item_number, item_number, item_name, pav_etiketei, barkodas2, count=1):
        self.uniq_item_number = uniq_item_number
        self.item_number = item_number
        self.item_name = item_name
        self.pav_etiketei = pav_etiketei
        self.barkodas2 = barkodas2
        self.count = count

    def __str__(self):
        return f"{self.count} vnt. \t{self.item_number}\t{self.pav_etiketei}"

def get_products(barcodes):
    connection_string = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=192.168.0.60;'
        r'DATABASE=ofisas;'
        r'UID=ofs_admin;'
        r'PWD=vasaris27ketvirtadienis2014'
    )

    placeholders = ', '.join('?' * len(barcodes))
    query = f"SELECT UniqItemNumber, ItemNumber, ItemName, PavEtiketei, BarKodas2 FROM SandelysPreke WHERE BarKodas2 IN ({placeholders})"

    products = []
    with pyodbc.connect(connection_string) as connection:
        cursor = connection.cursor()
        rows = cursor.execute(query, barcodes).fetchall()
        for row in rows:
            products.append(Product(*row))

    return products

def form_message(products):
    product_lines = "\n".join(str(product) for product in products)

    message_body = f"""Laba diena,
Noriu užsakyti į 950 parduotuvę:

{product_lines}

Ačiū.
"""
    message_signature = """

Pagarbiai,

D. Dikij
Programuotojas
"""

    return message_body + message_signature

def send_email(message):
    from_address = "dmitrijus@kosmelita.lt"
    password = "?+Dima*542"
    to_address = "dmitrijus@kosmelita.lt"
    subject = "Prekių užsakymas į 950 parduotuvę"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('mail.kosmelita.lt', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(from_address, password)
            smtp.send_message(msg)
            print(f"Sent email to {to_address}")
            print(message)
    except Exception as e:
        print(f"Error sending email: {e}")

def main(barcodes):
    print("Received barcodes:", barcodes)
    products = get_products(barcodes)
    
    if len(products) == 0:
        print("There are no products found.")
        return;
    print(f"Products retrieved: {len(products)}")
    message = form_message(products)
    print("Message:\n")
    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Barcodes')

    # Add arguments
    parser.add_argument('barcodes', nargs='+', type=str, help='Array of barcodes')

    # Parse command-line arguments
    args = parser.parse_args()

    # Pass barcodes to main() function
    main(args.barcodes)
