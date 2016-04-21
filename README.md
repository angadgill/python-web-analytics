# python-web-analytics
Simple cloud-based web analytics in Python.

##### How to test `pwanalytics.js`:
```
cd python-web-analytics
python -m SimpleHTTPServer 8000
```
Open a web browser and navigate to `localhost:8000/boilerplate-html/index.html`
Use the console to see that PyWebAnalytics has loaded with no errors.  

##### To run the `collector` server:
```
cd python-web-analytics/collector
python collector.py
```
This server accepts GET requests at this address: `localhost:5000/collect` and prints
data received as URL params to the terminal.


