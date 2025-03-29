from flask import Flask, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text










if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)