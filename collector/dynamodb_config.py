"""
DynamoDB table configuration

Author: Angad Gill
"""

from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table

DYNAMO_TABLES = [
    Table('pages', schema=[HashKey('key')]),
]
