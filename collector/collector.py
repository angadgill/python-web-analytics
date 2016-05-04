"""
Simple server to receive GET requests from pwanalysis.js
and dump all received data into a database.

Author: Angad Gill
"""

from flask import Flask, request
from flask.ext.dynamo import Dynamo

from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table

import time


app = Flask(__name__)
app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000


app.config['DYNAMO_TABLES'] = [
    Table('pages', schema=[HashKey('key')]),
]


dynamo = Dynamo(app)

# with app.app_context():
#     dynamo.create_all()
#     for table_name, table in dynamo.tables.iteritems():
#         print table_name, table


@app.route('/collect', methods=['GET'])
def index():
    pagename = request.args.get('pagename')
    time_stamp = time.time()
    user_id = 99999
    key = pagename + '_' + str(user_id) + '_' + str(time_stamp)
    print pagename
    dynamo.tables['pages'].put_item(data={
        'key': key,
        'pagename': pagename,
        'time': time_stamp,
        'user_id': user_id
    })
    return ""  # Super small response sent to client


if __name__ == '__main__':
    app.run(debug=True)