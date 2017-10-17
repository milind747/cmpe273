from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':u'Buy groceries',
        'description':u'milk,cheese,pizza,fruit',
        'done':False
    },
    {
        'id':2,
        'title':u'learn Phython',
        'description':u'need to find a good python tutorial on the web',
        'done':False
    }
]

@app.route("/todo/api/v1.0/tasks<int:task_id>", methods=['GET'])

def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})

if __name__=="__main__":
    app.run(debug=True)