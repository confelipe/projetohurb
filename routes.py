from app import app
from modules.product import *

@app.route('/api', methods=['GET'])
def status():
    return api()

@app.route('/api/bd', methods=['GET'])
def statusBD():
    return connectDb()

@app.route('/api/products', methods=['GET'])
def get():
    return getProducts()

@app.route('/api/products', methods=['POST'])
def post():
    return Product.saveProduct(request.json)

@app.route('/api/products/<product_id>', methods=['DELETE'])
def delete(product_id):
    return Product.deleteProduct(product_id)