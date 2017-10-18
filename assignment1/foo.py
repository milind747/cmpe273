# running it on localhost:5000
from flask import Flask, make_response, request
import rocksdb, uuid
import subprocess

app = Flask(__name__)


@app.route('/api/v1/scripts',methods=['POST'])
def save_file():
    inputdb = rocksdb.DB("cmpe273assn1.db",rocksdb.Options(create_if_missing = True))
    k = uuid.uuid4().hex
    a = request.files['data']
    mainfile = '/tmp/' + k + '.py'
    a.save(mainfile)
    inputdb.put(k.encode('utf-8'),mainfile.encode('utf-8'))
    return (k)


@app.route('/api/v1/scripts/<script_id>',methods=['GET'])
def call_file(script_id):
    inputdb = rocksdb.DB("cmpe273assn1.db",rocksdb.Options(create_if_missing = True))
    xy = inputdb.get(script_id.encode('utf-8'))
    tostr = str(xy)
    fnlstr=tostr[2:]
    fnlstr1="python3 " + fnlstr[0:len(fnlstr)-1]
    
    p = subprocess.Popen(fnlstr1, stdout=subprocess.PIPE, shell=True)
    #print p.communicate()
    return p.stdout.readline()


if __name__=="__main__":
    app.run(debug=True)


