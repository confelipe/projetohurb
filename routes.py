@app.route('/', methods=['GET'])
def index():
    return 'jsonify(devs), 200'