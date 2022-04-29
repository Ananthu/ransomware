from flask import Flask, render_template, request 

app = Flask(__name__) 
     
     
@app.route('/', methods = ['POST']) 
def store_key(): 
    data = request.json
    file_name = data.get('device_id')
    encryption_key = data.get('encryption_key')
    print(type(encryption_key))
    with open('./key_storage/{}'.format(file_name), 'w') as fp:
        fp.write(encryption_key)
    return ('', 204)

@app.route('/', methods = ['GET']) 
def get_key():
    data = request.json
    file_name = data.get('device_id')
    with open('./key_storage/{}'.format(file_name), 'r') as fp:
        data = fp.read()
    return {'password': data}
     
if __name__ == '__main__': 
    app.run(debug = True)