# python-web-analytics
Simple cloud-based web analytics in Python.

##### How to test `pwanalytics.js`:
```
cd python-web-analytics
python -m SimpleHTTPServer 8000
```
Open a web browser and navigate to `localhost:8000/boilerplate-html/index.html`
Use the console to see that PyWebAnalytics has loaded with no errors.  

##### How to run the `collector` server:
Install a local copy of DynamoDB. See guide [here](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html).
Set environment variables as follows:

```
export DYNAMO_ENABLE_LOCAL=True  
export DYNAMO_LOCAL_HOST='localhost'  
export DYNAMO_LOCAL_PORT=8080  
```

Run the DynamoDB local instance:
```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port 8080
```

To run the `collector server`, run commands as follows:  
```
cd python-web-analytics/collector
python collector.py
```
This server accepts GET requests at this address: `localhost:5000/collect` and prints
data received as URL params to the terminal.  