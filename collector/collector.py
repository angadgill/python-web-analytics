"""
Simple server to receive GET requests from pwanalysis.js
and dump all received data into a database.

Author: Angad Gill
"""

from flask import Flask, request
from flask.ext.dynamo import Dynamo
import dynamodb_config
import time


app = Flask(__name__)
app.config['DYNAMO_TABLES'] = dynamodb_config.DYNAMO_TABLES
dynamo = Dynamo(app)  # Assumes that DynamoDB tables are already setup


@app.route('/collect', methods=['GET'])
def index():
    pagename = str(request.args.get('pagename'))
    time_stamp = time.time()
    # TODO: Replace 99999 below with actual user_id
    user_id = 99999
    key = pagename + '_' + str(user_id) + '_' + str(time_stamp)
    print key
    with app.app_context():
        dynamo.tables['pages'].put_item(data={
            'key': key,
            'pagename': pagename,
            'time': time_stamp,
            'user_id': user_id
        })
    return ""  # Super small response sent to client


if __name__ == '__main__':
    app.run(debug=True)