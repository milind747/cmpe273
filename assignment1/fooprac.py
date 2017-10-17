from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/todo/api/v1.0/tasks", methods=['POST'])

def post_data():
    task = {
        print ("Helloooo")
    }
    return jsonify({'task': task}), 201

if __name__=="__main__":
    app.run(debug=True)