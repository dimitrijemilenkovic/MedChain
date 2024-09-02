class PatientData:
    def __init__(self, patient_id, name, diagnosis, treatment):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.treatment = treatment

    def to_dict(self):
        return {
            'patient_id': self.patient_id,
            'name': self.name,
            'diagnosis': self.diagnosis,
            'treatment': self.treatment
        }
