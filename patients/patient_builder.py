from .models import PatientRecords, MedicineInformation, Dosage, MedicinePrescription
from .patient_dto import DosageObject, PatientObject, MedicineObject, MedicinePrescriptionObject

class PatientBuilder:
    @staticmethod
    def resolve_get_patient(id):
        if id is not None:
            patient_info=PatientRecords.objects.filter(patientID=id).first()
            if patient_info:
                return PatientObject(
                    patientID = patient_info.patientID,
                    first_name = patient_info.first_name,
                    last_name = patient_info.last_name,
                    age = patient_info.age,
                    weight = patient_info.weight,
                    height = patient_info.height,
                    medication = PatientBuilder.resolve_get_medicine(id =patient_info.medication.medicine_uid),
                    dosage = PatientBuilder.resolve_get_dosage(id =patient_info.dosage.dose_uid),
                    prescrition = PatientBuilder.resolve_get_prescritpion(id = patient_info.prescrition.prescriptionID),
                    patient_created_date = patient_info.patient_created_date,
                )
            else:
                return PatientObject()
        else:
            return PatientObject()

    @staticmethod
    def resolve_get_medicine(id):
        if id is not None:
            print("I can reach here wao that nice")
            medicine_info = MedicineInformation.objects.filter(medicine_uid = id).first()
            print(" This is the medeeee :" , medicine_info.name)
            if medicine_info:
                return MedicineObject (
                    id = medicine_info.pk,
                    medicine_uid = medicine_info.medicine_uid,
                    name = medicine_info.name,
                    description = medicine_info.description,
                    manufacturer = medicine_info.manufacturer,
                    medicine_type = medicine_info.medicine_type,
                    medicine_created_date = medicine_info.medicine_created_date,
                )
            else:
                return MedicineObject()
        else:
            return MedicineObject()
    @staticmethod
    def resolve_get_dosage(id):
        if id is not None:
            dosage = Dosage.objects.filter(dose_uid = id).first()
            print("I get this at hereeeee : ", dosage.medicine.medicine_uid)
            if dosage:
                return DosageObject(
                    id = dosage.pk,
                    dose_uid = dosage.dose_uid,
                    medicine = PatientBuilder.resolve_get_medicine(id = dosage.medicine.medicine_uid),
                    amount = dosage.amount,
                    frequency = dosage.frequency,
                    dose_created_date = dosage.dose_created_date
                )
            else:
                return DosageObject()
        else:
            return DosageObject()
    @staticmethod
    def resolve_get_prescritpion(id):
        if id is not None:
            prescription = MedicinePrescription.objects.filter(prescriptionID = id).first()
            if prescription:
                return MedicinePrescriptionObject(
                    id = prescription.pk,
                    prescriptionID = prescription.prescriptionID,
                    prescription_name = prescription.prescription_name,
                    dosage = PatientBuilder.resolve_get_dosage(id = prescription.dosage.dose_uid),
                    medicine = PatientBuilder.resolve_get_medicine(id = prescription.medicine.medicine_uid),
                    prescription_created_date = prescription.prescription_created_date,
                )
            else:
                return MedicinePrescriptionObject()
        else:
            return MedicinePrescriptionObject()
            