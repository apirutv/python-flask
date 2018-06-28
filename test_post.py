#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/first_call', methods=['POST'])
def first_callback():
    if request.method == 'POST':
        result = request.data
        id = request.args.get("id")
        name = request.form.get('name')
        client_ip = request.remote_addr
        print('client IP:',client_ip)
        print('id:', id)
        print('name:', name)
        print('client data:',request.json)

    return "OK"


@app.route('/second_call', methods=['GET'])
def second_callback():
    if request.method == 'GET':
         #....
         pass

    return "OK"

if __name__ == '__main__':
    app.debug = True
    app.run("127.0.0.1")

