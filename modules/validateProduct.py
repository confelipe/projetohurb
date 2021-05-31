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
        sku = data[0]['sku'].strip()
        if productTable.selectProductSku(sku):
            message = {
                'errorText' : 'SKU '+sku+' already registered'
            }
        #validates if the product contains attributes
        if("attributes" in data[0]):
            attributes = True
        #validates if the product contains barcodes
        if("barcodes" in data[0]):
            validateBarcode = barcodeTable.select(data[0]['barcodes'])
            if(validateBarcode != None):
                message = {
                    'errorText' : 'Barcode '+str(data[0]['barcodes'])+' already registered for product '+str(validateBarcode[0])
                }
            barcodes = True
        try:
            price = float(data[0]['price'])
        except ValueError:
            message = {
                'errorText' : 'price is not valid value, insert a price valid. ex.: 0.00 '
            }
        
        return message, barcodes, attributes