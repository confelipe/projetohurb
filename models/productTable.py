from models.connectDb import connection
from models.barcodeTable import barcodeTable
from models.attributeTable import attributeTable

import time

class productTable:
    def selectProductSku(sku):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(sku) FROM product WHERE sku = %(sku)s;", ({'sku': sku,}))
        count = cursor.fetchone()
        count = count[0]
        cursor.close()
        conn.close()
        if(count != 0) :
            ifExists = True
            return ifExists
        else :
            ifExists = False
            return ifExists

    def save(data, barcodes, attribute):
        conn = connection()
        cursor = conn.cursor()
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        for product in data:
            title = product['title']
            sku = product['sku']
            description = product['description']
            price = product['price']
        cursor.execute("INSERT INTO product (title, sku, description, price, created, last_updated) VALUES (%(title)s, %(sku)s, %(description)s, %(price)s, %(created)s, %(updated)s);", ({'title': title, 'sku' : sku, 'description' : description, 'price' : price, 'created' : date, 'updated' : date,}))
        
        conn.commit()
        cursor.execute("SELECT LAST_INSERT_ID();")
        insert = cursor.fetchone()
        insert = int(''.join(map(str, insert)))
        cursor.close()
        conn.close()
        if(barcodes):
            barcodeTable.save(insert, data[0]['barcodes'])
        if(attribute):
            attributeTable.save(insert, data[0]['attributes'])
        return insert

    def delete(product_id):
        barcodeTable.delete(product_id)
        attributeTable.delete(product_id)
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product WHERE product_id = %(product_id)s', ({'product_id':product_id,}))
        conn.commit()
        cursor.close()
        conn.close()