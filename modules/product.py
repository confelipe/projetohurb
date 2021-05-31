from flask import jsonify, request, json
from modules.validateProduct import validateProduct
from models.productTable import productTable

def api():
    api = [
        {
            "name" : "Product API",
            "version" : "1.0.0"
        }
    ]

    return jsonify(api), 200

#def connectDb():
#    connect = connection()
#    cursor = connect.cursor()
#    cursor.execute("select database();")
#    result = cursor.fetchall()
#    data = [
#        {
#            'statusCode' : 200,
#            'action' : 'connect to db',
#            'data' : result
#        }
#    ]
#    return jsonify(data), 200

class Product:
    
    def getProducts():
        return jsonify(devs), 200

    def saveProduct(data):
        #validate payload
        validates = validateProduct.validatePayload(data)
        if validates[0]:
            return jsonify(validates[0]), 400
        save = productTable.save(data, validates[1], validates[2])
        return jsonify(save), 201