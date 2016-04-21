"""
Simple server to receive GET requests from pwanalysis.js
and dump all received data into a database.

Author: Angad Gill
"""

from flask import Flask, request
app = Flask(__name__)


@app.route('/collect', methods=['GET'])
def index():
    print request.args
    return "Collected!"


if __name__ == '__main__':
    app.run(debug=True)