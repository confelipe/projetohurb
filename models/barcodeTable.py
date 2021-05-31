from models.connectDb import connection

class barcodeTable:
    def select(barcode):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product_barcode WHERE barcode = %(barcode)s", ({'barcode':barcode,}))
        select = cursor.fetchone()
        return select
        
    def save(product_id, barcode):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product_barcode (product_id, barcode) VALUES (%(product_id)s, %(barcode)s);", ({'product_id': product_id, 'barcode' : barcode,}))
        conn.commit()

    def delete(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product_barcode WHERE product_id = %(product_id)s;', ({'product_id':product_id,}))
        conn.commit()
        cursor.close()
        conn.close()