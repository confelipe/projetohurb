from flask import Flask, jsonify

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Rafael Marques',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Robert Hrosher',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'John Delare',
        'lang': 'python'
    },
    {
        'id': 4,
        'name': 'John Doe',
        'lang': 'node'
    }
]

@app.route('/', methods=['GET'])
def index():
    return jsonify(devs), 200


@app.route('/api/products', methods=['GET'])
def index():
    return jsonify(devs), 200

if __name__ == '__main__':
    app.run(debug=True)