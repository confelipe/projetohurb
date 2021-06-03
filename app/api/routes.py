from app import app
from modules.product import *

#route for all products
@app.route('/api/products', methods=['GET'])
def get():
    args = request.args
    return Product.getProducts(args)
#route for filter by product id
@app.route('/api/products/<product_id>', methods=['GET'])
def getId(product_id):
    args = request.args
    typeCode = 'product_id'
    return Product.getProductsId(args, product_id, typeCode)
#route for filter by sku 
@app.route('/api/products/<sku>/sku', methods=['GET'])
def getSku(sku):
    args = request.args
    typeCode = 'sku'
    return Product.getProductsId(args, sku, typeCode)
#route for filter by barcode    
@app.route('/api/products/<barcode>/barcode', methods=['GET'])
def getBarcode(barcode):
    args = request.args
    typeCode = 'barcode'
    return Product.getProductsId(args, barcode, typeCode)
#route for put the product
@app.route('/api/products/<product_id>', methods=['PUT'])
def put(product_id):
    return Product.updateProduct(product_id, request.json)
#route for post the product
@app.route('/api/products', methods=['POST'])
def post():
    return Product.saveProduct(request.json)
#route for delete the product
@app.route('/api/products/<product_id>', methods=['DELETE'])
def delete(product_id):
    return Product.deleteProduct(product_id)