# from flask import Flask, jsonify
# import requests
#
# app = Flask(__name__)
#
# @app.route('/sync', methods=['POST'])
# def sync():
#     try:
#         response = requests.get('http://127.0.0.1:5080/get_chain')
#         if response.status_code == 200:
#             chain_data = response.json()
#             return jsonify({"message": "Synchronization successful", "data": chain_data}), 200
#     except Exception as e:
#         return jsonify({"message": "Synchronization failed", "error": str(e)}), 500
#
# if __name__ == "__main__":
#     app.run(port=5001)
