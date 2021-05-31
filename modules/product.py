from flask import jsonify, request, json
from modules.validateProduct import validateProduct
from models.productTable import productTable
from models.barcodeTable import barcodeTable
from models.attributeTable import attributeTable

class Product:
    
    def getProducts(args):
        selectProducts = productTable.selectProduct()
        items = []
        for products in selectProducts:
            selectBarcode = barcodeTable.select(products[0])
            selectAttribute = attributeTable.select(products[0])
            attributes = []
            if(selectAttribute != None):
                for attribute in selectAttribute:
                    attributes.append({
                        "name" : attribute[0],
                        "value" : attribute[1]
                    })
            items.append({
                'productId' : products[0],
                'title' : products[1],
                'sku' : products[2],
                'barcodes' : selectBarcode,
                'description' : products[3],
                'attributes' : [attributes],
                'price' : float(products[4])
            })
        products = {
            "totalCount" : len(items),
            "args" : args,
            "items" : items
        }
        filterFields = Product.filterFields(args['fields'], items)
        return jsonify(filterFields), 200

    def saveProduct(data):
        #validate payload
        validates = validateProduct.validatePayload(data)
        if validates[0]:
            return jsonify(validates[0]), 400
        #save product
        save = productTable.save(data, validates[1], validates[2])
        return jsonify(save), 201

    def deleteProduct(product_id):
        delete = productTable.delete(product_id)
        return jsonify(), 200
    
    def updateProduct(product_id, data):
        validates = validateProduct.validatePayloadUpdate(product_id, data)
        if('error' in validates and validates['error']['message'] != False):
            return validates['error']['message']
        update = productTable.update(product_id, validates, data)
        return jsonify(), 200

    def filterFields(args, items):
        args = args.split(',')
        product = []
        number = 0
        for item in items:
            for arg in args:
                number = 0
                product.append(str(arg)+' : '+str(item[arg]))
        return product