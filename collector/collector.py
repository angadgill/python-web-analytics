"""
Simple server to receive GET requests from pwanalysis.js
and dump all received data into a database.

Author: Angad Gill
"""

from flask import Flask, request, send_file
from flask.ext.dynamo import Dynamo
import dynamodb_config
import time

from multiprocessing import Pool


app = Flask(__name__)
app.config['DYNAMO_TABLES'] = dynamodb_config.DYNAMO_TABLES
dynamo = Dynamo(app)  # Assumes that DynamoDB tables are already setup

process_pool = None

def send_data_to_dynamodb(data):
    """
    Send data to DynamoDB.
    :param data
    :return:
    """
    pagename, time_stamp, user_id = data

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


@app.route('/', methods=['GET'])
def index():
    pagename = request.args.get('pagename')
    time_stamp = time.time()
    user_id = request.args.get('user_id')
    data = pagename, time_stamp, user_id

    if pagename:  # pagename is not None
        print "Page visit at:", pagename
        # Use process pool to send data to DynamoDB so that index returns quickly
        process_pool.apply_async(send_data_to_dynamodb, [data])
        
    return send_file('__hello.gif')  # Super small web beacon response


if __name__ == '__main__':
    process_pool = Pool(processes=4)
    try:
        # insert production server deployment code
        app.run()
    except KeyboardInterrupt:
        process_pool.close()
        process_pool.join()