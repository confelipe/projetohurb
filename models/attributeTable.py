from models.connectDb import connection

class attributeTable:
    def save(product_id, attributes):
        conn = connection()
        cursor = conn.cursor()
        for attribute in attributes:
            name = attribute['name']
            value = attribute['value']
            cursor.execute("INSERT INTO product_attribute (product_id, name, value) VALUES (%(product_id)s, %(name)s, %(value)s);", ({'product_id': product_id, 'name' : name, 'value': value,}))
            conn.commit()

    def delete(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product_attribute WHERE product_id = %(product_id)s', ({'product_id':product_id,}))
        conn.commit()
        cursor.close()
        conn.close()