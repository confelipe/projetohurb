from mysql.connector import connect, Error
from flask import jsonify

def connection():
    conn = connect(host="product-api-mysql-service", database='hurb_test_assignment', user='product', password='product')
    if conn.is_connected():
        return conn
    else:
        error = {
            "errorText" : "Does not possible connect to db"
        }
        return jsonify(error), 500