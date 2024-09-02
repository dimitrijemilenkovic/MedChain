from flask import Flask
from server.routes import configure_routes
from logging_middleware import log_request_response

app = Flask(__name__)

configure_routes(app)

log_request_response(app)

if __name__ == '__main__':
    app.run(debug=True)

