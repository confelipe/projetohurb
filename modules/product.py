from flask import jsonify, request, json
from modules.validateProduct import validateProduct
from models.productTable import productTable
from models.barcodeTable import barcodeTable
from models.attributeTable import attributeTable

class Product:
    
    def getProducts(args):
        if('start' in args):
            start = args['start']
        else:
            start = 0
        if('num' in args):
            num = args['num']
        else:
            num = False
        selectProducts = productTable.selectProduct(start, num)
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
            "items" : items
        }
        if('fields' in args):
            filterFields = Product.filterFields(args['fields'], items)
            products = {
                "totalCount" : len(items),
                "items" : filterFields
            }
            return jsonify(products), 200
        else:
            return jsonify(products), 200

    def getProductsId(args, code, typeCode):
        if(typeCode == 'product_id'):
            selectProducts = productTable.selectProductId(int(code))
            if(selectProducts == None):
                message = {
                    'errorText' : 'Can’t find product ('+code+')'
                }
                return message
            selectBarcode = barcodeTable.select(int(code))
            selectAttribute = attributeTable.select(int(code))
        if(typeCode == 'sku'):
            selectProducts = productTable.selectProductSku(code)
            if(selectProducts == None):
                message = {
                    'errorText' : 'Can’t find SKU ('+code+')'
                }
                return message
            selectBarcode = barcodeTable.select(int(selectProducts[0]))
            selectAttribute = attributeTable.select(int(selectProducts[0]))
        if(typeCode == 'barcode'):
            selectBarcode = barcodeTable.selectBarcode(int(code))
            if(selectBarcode == None):
                message = {
                    'errorText' : 'Can’t find barcode ('+code+')'
                }
                return message
            selectProducts = productTable.selectProductId(int(selectBarcode[0]))
            selectAttribute = attributeTable.select(int(selectBarcode[0]))
        items = []
        attributes = []
        if(selectAttribute != None):
            for attribute in selectAttribute:
                attributes.append({
                    "name" : attribute[0],
                    "value" : attribute[1]
                })
        items.append({
            'productId' : selectProducts[0],
            'title' : selectProducts[1],
            'sku' : selectProducts[2],
            'barcodes' : selectBarcode,
            'description' : selectProducts[3],
            'attributes' : [attributes],
            'price' : float(selectProducts[4])
        })
        if('fields' in args):
            filterFields = Product.filterFields(args['fields'], items)
            return jsonify(filterFields), 200
        else:
            return jsonify(items), 200

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
        fieldsDefault = ['title','sku','barcodes','description','attributes','price','productId']
        filterFields = [p for p in fieldsDefault if p not in args]
        product = []
        number = 0
        for item in items:
            [item.pop(key) for key in filterFields]
            product.append(item)
        return product