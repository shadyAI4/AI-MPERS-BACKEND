import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from django.db.models import Q
from .patient_dto import PatientResponseObject, MedicineResponseObject, PatientObject, MedicineObject, DosageObject, DosageResponseObject , MedicinePrescriptionObject, MedicinePrescriptionResponseObject
from uaa_dto.Response import ResponseObject
from .models import PatientRecords, MedicineInformation, MedicinePrescription, Dosage


class Query(ObjectType):
    
    get_all_patient_records = graphene.Field(PatientResponseObject)
    get_patient_records =graphene.Field(PatientObject, patientID= graphene.String())
    
    def resolve_get_all_patient_records(self, info):
        all_patients = PatientRecords.objects.all().values('patientID')
        return PatientResponseObject( response = ResponseObject.get_response(id='6'), data = all_patients)

    def resolve_get_patient_records(self, info, patientID):
        patient_data = PatientRecords.objects.get(patientID = patientID)
        return self(response = ResponseObject.get_response(id= '6'), data = patient_data)
    

schema = graphene.Schema(query=Query)