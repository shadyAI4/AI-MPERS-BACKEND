import graphene
from .models import PatientRecords, MedicineInformation, Dosage
from uaa_dto.Response import ResponseObject

class PatientInputObject(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    age = graphene.Int()
    weight = graphene.Decimal()
    height = graphene.Decimal()
    medication = graphene.String()
    dosage = graphene.String()
    prescrition = graphene.String()

class UpdatePatientInputObject(graphene.InputObjectType):
    patientID = graphene.String()
    medication = graphene.String()
    dosage = graphene.String()
    prescrition = graphene.String()
    



    
# ************************** MEDICINE DTO ***********
class MedicineInputObject(graphene.InputObjectType):
    
    name = graphene.String()
    description = graphene.String()
    manufacturer = graphene.String()
    medicine_type = graphene.String()

class MedicineObject(graphene.ObjectType):
    id = graphene.ID()
    medicine_uid = graphene.String()
    name = graphene.String()
    description = graphene.String()
    manufacturer = graphene.String()
    medicine_type = graphene.String()
    medicine_created_date = graphene.String()

class MedicineResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(MedicineObject)
    
# ******************** DOSAGE*****************
    
class DosageInputObject(graphene.InputObjectType):
    medicine = graphene.String()
    amount = graphene.String()
    frequency = graphene.String()

class DosageObject(graphene.ObjectType):
    id = graphene.ID()
    dose_uid = graphene.String()
    medicine = graphene.Field(MedicineObject)
    amount = graphene.String()
    frequency = graphene.String()
    dose_created_date = graphene.String()
    
class DosageResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(DosageObject)
    
# ********************** PRESRCITPION ******************

class MedicinePrescritpionInputObject(graphene.InputObjectType):
    prescription_name = graphene.String()
    dosage = graphene.String()
    medicine = graphene.String()

class MedicinePrescriptionObject(graphene.ObjectType):
    id = graphene.ID()
    prescriptionID = graphene.String()
    prescription_name = graphene.String()
    dosage = graphene.Field(DosageObject)
    medicine = graphene.Field(MedicineObject)
    prescription_created_date = graphene.String()
    
class MedicinePrescriptionResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(MedicinePrescriptionObject)
    
    
class PatientObject(graphene.ObjectType):
    patientID = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    age = graphene.Int()
    weight = graphene.Decimal()
    height = graphene.Decimal()
    patient_created_date = graphene.String()
    medication = graphene.Field(MedicineObject)
    dosage = graphene.Field(DosageObject)
    prescrition = graphene.Field(MedicinePrescriptionObject)
    
class PatientResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObject)
    data = graphene.List(PatientObject)
    