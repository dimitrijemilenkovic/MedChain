from flask import request, jsonify, render_template, redirect, url_for
from blockchain.blockchain import Blockchain
from blockchain.models import PatientData

blockchain = Blockchain()


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/add_patient_data', methods=['POST'])
    def add_patient_data():
        data = {
            'patient_id': request.form['patient_id'],
            'name': request.form['name'],
            'diagnosis': request.form['diagnosis'],
            'treatment': request.form['treatment']
        }
        patient = PatientData(**data)
        blockchain.add_block(patient.to_dict())
        return jsonify({"message": "Data added to blockchain"}), 200

    @app.route('/delete_block/<int:index>', methods=['POST'])
    def delete_block(index):
        blockchain.mark_block_as_deleted(index)
        return redirect(url_for('get_chain'))

    @app.route('/get_chain', methods=['GET'])
    def get_chain():
        chain_data = []
        for block in blockchain.get_active_chain():
            chain_data.append({
                "index": block.index,
                "previous_hash": block.previous_hash,
                "timestamp": block.timestamp,
                "data": block.data,
                "hash": block.hash
            })
        return render_template('chain.html', chain_data=chain_data)

    @app.route('/search_patient', methods=['GET'])
    def search_patient():
        patient_id = request.args.get('patient_id')

        if not patient_id:
            return "Patient ID is required", 400
        patient_data = []
        for block in blockchain.get_active_chain():
            if block.data.get('patient_id') == patient_id:
                patient_data.append({
                    "index": block.index,
                    "previous_hash": block.previous_hash,
                    "timestamp": block.timestamp,
                    "data": block.data,
                })

        return render_template('patient_data.html', patient_data=patient_data)

