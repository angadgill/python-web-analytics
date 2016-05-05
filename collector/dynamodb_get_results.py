"""
Use this script to print results from DynamoDB in terminal.

Author: Angad Gill
"""

from flask import Flask
from flask.ext.dynamo import Dynamo
import dynamodb_config

app = Flask(__name__)
app.config['DYNAMO_TABLES'] = dynamodb_config.DYNAMO_TABLES
dynamo = Dynamo(app)

with app.app_context():
    table = dynamo.tables['pages']
    results = table.scan()
    for result in results:
        pagename = result['pagename']
        count = result['count']
        unique_users = len(set(result['user_id']))  # Convert to set to count unique
        print "Pagename: %s, \t count: %d, \t unique users: %d" % \
              (pagename, count, unique_users)
