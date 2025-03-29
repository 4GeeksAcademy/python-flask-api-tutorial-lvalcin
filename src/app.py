from flask import Flask, jsonify
from flask import Flask, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    updated_list = todos.pop(position)
    return jsonify(todos)

    my_list = [1, 2, 3, 2]
    my_list.remove(2)
    print(my_list)  # Output: [1, 3, 2]









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)