from flask import jsonify, request, json
from models.productTable import productTable
from models.barcodeTable import barcodeTable

class validateProduct:
    def validatePayload(data):
        message = False
        attributes = False
        barcodes = False
        #validates if title is present
        if ("title" not in data[0]):
            message = {
                'errorText' : 'title is obrigatory'
            }
        #valid if sku is present
        if ("sku" not in data[0]):
            message = {
                'errorText' : 'sku is obrigatory'
            }
        #validates if sku exist in database
        #retire space of sku (start or end)
        sku = data[0]['sku'].strip()
        if productTable.countProductSku(sku):
            message = {
                'errorText' : 'SKU '+sku+' already registered'
            }
        #validates if the product contains attributes
        if("attributes" in data[0]):
            attributes = True
        #validates if the product contains barcodes
        if("barcodes" in data[0]):
            validateBarcode = barcodeTable.selectBarcode(data[0]['barcodes'])
            if(validateBarcode != None):
                message = {
                    'errorText' : 'Barcode '+str(data[0]['barcodes'])+' already registered for product '+str(validateBarcode[0])
                }
            barcodes = True
        if("price" in data[0]):
            try:
                price = float(data[0]['price'])
            except ValueError:
                message = {
                    'errorText' : 'price is not valid value, insert a price valid. ex.: 0.00 '
                }
        
        return message, barcodes, attributes
    
    def validatePayloadUpdate(product_id, data):
        product = False
        attributes = False
        barcodes = False
        message = False
        #validates if product is altered
        if ("title" in data[0] or "sku" in data[0] or "description" in data[0] or "price" in data[0]):
            product = True
        if("attributes" in data[0]):
            attributes = True
        #validates if the product contains barcodes
        if("barcodes" in data[0]):
            validateBarcode = barcodeTable.selectBarcode(data[0]['barcodes'])
            if(validateBarcode != None and int(product_id) != validateBarcode[0]):
                message = {
                    'errorText' : 'Barcode '+str(data[0]['barcodes'])+' already registered for product '+str(validateBarcode[0])
                }
            barcodes = True
        if("price" in data[0]):
            try:
                price = float(data[0]['price'])
            except ValueError:
                message = {
                    'errorText' : 'price is not valid value, insert a price valid. ex.: 0.00 '
                }
        #validates if sku exist in database
        #retire space of sku (start or end)
        if('sku' in data[0]):
            sku = data[0]['sku'].strip()
        else:
            sku = None
        selectSku = productTable.selectProductSku(sku)
        if (selectSku != None and sku == selectSku[2] and int(product_id) != selectSku[0]):
            message = {
                'errorText' : 'SKU '+sku+' already registered'
            }
        validates = {
                'product' : product,
                'barcodes' : barcodes,
                'attributes' : attributes,
                'error' : {
                    'message' : message
                }
            }
        
        return validates