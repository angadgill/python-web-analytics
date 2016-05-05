"""
Use this script to setup DynamoDB tables.

Author: Angad Gill
"""

from flask import Flask
from flask.ext.dynamo import Dynamo
import dynamodb_config

app = Flask(__name__)
app.config['DYNAMO_TABLES'] = dynamodb_config.DYNAMO_TABLES
dynamo = Dynamo(app)

with app.app_context():
    dynamo.create_all()

print "Done!"