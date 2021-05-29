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
    return saveProduct(request.json)