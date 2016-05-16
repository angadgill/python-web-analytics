"""
Simple server to receive GET requests from pwanalysis.js
and dump all received data into a database.

Author: Angad Gill
"""

from flask import Flask, request, send_file
from flask.ext.dynamo import Dynamo
import dynamodb_config
import time


app = Flask(__name__)
app.config['DYNAMO_TABLES'] = dynamodb_config.DYNAMO_TABLES
dynamo = Dynamo(app)  # Assumes that DynamoDB tables are already setup


@app.route('/', methods=['GET'])
def index():
    pagename = request.args.get('pagename')
    time_stamp = time.time()
    user_id = request.args.get('user_id')

    if pagename:  # pagename is not None
        print "Page visit at:", pagename
        with app.app_context():
            table = dynamo.tables['pages']

            # Update existing pagename value
            # Assumes that pagename is the key
            if table.has_item(pagename=pagename):
                print "Updating existing entry..."
                item = table.get_item(pagename=pagename)
                item['time'] += [time_stamp]
                item['user_id'] += [user_id]
                item['count'] += 1
                table.put_item(item, overwrite=True)
            else:
                # If pagename doesn't exist, create a new one
                print "Creating new entry for page..."
                table.put_item(data={
                    'pagename': pagename,
                    'time': [time_stamp],
                    'user_id': [user_id],
                    'count': 1
                })
    return send_file('__hello.gif')  # Super small web beacon response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
