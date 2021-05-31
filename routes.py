from app import app
from modules.product import *

#route for all products
@app.route('/api/products', methods=['GET'])
def get():
    args = request.args
    return Product.getProducts(args)
#route for filter by product id
@app.route('/api/products/<product_id>', methods=['GET'])
def getId():
    args = request.args
    return Product.getProducts(args, product_id)
#route for filter by sku 
@app.route('/api/products/<sku>/sku', methods=['GET'])
def getSku():
    args = request.args
    return Product.getProducts(args, sku)
#route for filter by barcode    
@app.route('/api/products/<barcode>/barcode', methods=['GET'])
def getBarcode():
    args = request.args
    return Product.getProducts(args, barcode)
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