from models.connectDb import connection

class attributeTable:
    def select(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, value FROM product_attribute WHERE product_id = %(product_id)s", ({'product_id':product_id,}))
        select = cursor.fetchall()
        return select

    def selectName(product_id, name):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, value FROM product_attribute WHERE name = %(name)s AND product_id = %(product_id)s", ({'name':name, 'product_id':int(product_id),}))
        select = cursor.fetchone()
        return select

    def save(product_id, attributes):
        conn = connection()
        cursor = conn.cursor()
        for attribute in attributes:
            name = attribute['name']
            value = attribute['value']
            validateIfExists = attributeTable.selectName(product_id, name)
            if(validateIfExists != None):
                cursor.execute("UPDATE product_attribute SET value = %(value)s WHERE name = %(name)s AND product_id = %(product_id)s", ({'value':value,'name':name,'product_id':int(product_id),}))
            else:
                cursor.execute("INSERT INTO product_attribute (product_id, name, value) VALUES (%(product_id)s, %(name)s, %(value)s);", ({'product_id': product_id, 'name' : name, 'value': value,}))
            conn.commit()

    def delete(product_id):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product_attribute WHERE product_id = %(product_id)s', ({'product_id':product_id,}))
        conn.commit()
        cursor.close()
        conn.close()