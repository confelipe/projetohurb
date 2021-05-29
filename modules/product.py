from flask import jsonify, request
from models.connectDb import connection

def api():
    api = [
        {
            "name" : "Product API",
            "version" : "1.0.0"
        }
    ]

    return jsonify(api), 200

def connectDb():
    connect = connection()
    cursor = connect.cursor()
    cursor.execute("select database();")
    result = cursor.fetchall()
    data = [
        {
            'statusCode' : 200,
            'action' : 'connect to db',
            'data' : result
        }
    ]
    return jsonify(data), 200

def getProducts():
    return jsonify(devs), 200

def saveProduct(data):
    return jsonify(data), 201