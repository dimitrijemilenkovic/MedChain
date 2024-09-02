import logging
from flask import request

# Podesi osnovno logovanje
logging.basicConfig(filename='app.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(message)s')

def log_request_response(app):
    @app.before_request
    def log_request():
        if not request.path.startswith('/static/'):  # Izuzmi statičke fajlove iz logovanja
            logging.info(f"Request: {request.method} {request.url} {request.data}")

    @app.after_request
    def log_response(response):
        if not request.path.startswith('/static/'):  # Izuzmi statičke fajlove iz logovanja
            logging.info(f"Response: {response.status} {response.data.decode('utf-8')}")
        return response
