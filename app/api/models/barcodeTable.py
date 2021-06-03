from models.connectDb import connection

class barcodeTable:
    def select(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product_barcode WHERE product_id = %(product_id)s", ({'product_id':product_id,}))
        select = cursor.fetchone()
        return select
    
    def selectBarcode(barcode):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product_barcode WHERE barcode = %(barcode)s", ({'barcode':barcode,}))
        select = cursor.fetchone()
        return select
        
    def save(product_id, barcode):
        conn = connection()
        cursor = conn.cursor()
        validateIfExist = barcodeTable.select(product_id)
        if(validateIfExist != None):
            cursor.execute("UPDATE product_barcode SET barcode = %(barcode)s WHERE product_id = %(product_id)s", ({'barcode':barcode, 'product_id':product_id,}))
        else:
            cursor.execute("INSERT INTO product_barcode (product_id, barcode) VALUES (%(product_id)s, %(barcode)s);", ({'product_id': product_id, 'barcode' : barcode,}))
        conn.commit()

    def delete(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product_barcode WHERE product_id = %(product_id)s;', ({'product_id':product_id,}))
        conn.commit()
        cursor.close()
        conn.close()