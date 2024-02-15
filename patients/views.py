from django.shortcuts import render
import graphene
from graphene_federation import build_schema
from patients.patient_builder import PatientBuilder
from uaa_dto.Response import ResponseObject
from .models import PatientRecords, MedicinePrescription, Dosage, MedicineInformation
from .patient_dto import PatientInputObject, PatientResponseObject, PatientObject, MedicineInputObject, MedicinePrescriptionResponseObject, MedicineObject, MedicinePrescriptionObject, MedicinePrescritpionInputObject, MedicineResponseObject, DosageInputObject, DosageObject, DosageResponseObject, UpdatePatientInputObject

# Create your views here.

class CreatePatientRecordsMutation(graphene.Mutation):
    class Arguments:
        input = PatientInputObject(required = True)
    response = graphene.Field(ResponseObject)
    data = graphene.Field(PatientObject)
    
    @classmethod
    def mutate(self, root, info, input):
       
        patient = PatientRecords.objects.create(
            first_name = input.first_name,
            last_name = input.last_name,
            age = input.age,
            weight = input.weight,
            height = input.height,
        )
        data = PatientBuilder.resolve_get_patient(id = patient.patientID)
        return self(response = ResponseObject.get_response(id ='5'), data= data)

class UpdatePatientRecordsMutation(graphene.Mutation):
    class Arguments:
        input = UpdatePatientInputObject(required = True)
    response = graphene.Field(ResponseObject)
    data = graphene.Field(PatientObject)
    
    @staticmethod
    
    def mutate(self, root,info, input):
        medication = MedicineInformation.objects.filter(medicine_uid = input.medication).first()
        dosage = Dosage.objects.filter(dose_uid = input.dosage).first()
        prescrition = MedicinePrescription.objects.filter(prescriptionID = input.prescrition).first()
        patient_data = PatientRecords.objects.get(patientID = input.patientID)
        patient_data.medication = medication
        patient_data.dosage = dosage
        patient_data.prescrition = prescrition
        patient_data.save()
        data = PatientBuilder.resolve_get_patient(id = patient_data.patientID)
        return self(response = ResponseObject.get_response(id='6'), data = data)

class CreateMedicineMutation(graphene.Mutation):
    class Arguments:
        input = MedicineInputObject(required= True)
    response = graphene.Field(ResponseObject)
    data = graphene.Field(MedicineObject)
    
    @classmethod
    def mutate(self, root, info, input):
        medicine = MedicineInformation.objects.create(
            name = input.name,
            description = input.description,
            manufacturer = input.manufacturer,
            medicine_type = input.medicine_type,
        )
        data = PatientBuilder.resolve_get_medicine(id = medicine.medicine_uid)
        return self( response = ResponseObject.get_response(id='6'), data = data)

class CreateDosageMutation(graphene.Mutation):
    class Arguments:
        input = DosageInputObject(required= True)
    
    response = graphene.Field(ResponseObject)
    data = graphene.Field(DosageObject)
    
    @classmethod
    def mutate(self, root, info, input):
        medicine = MedicineInformation.objects.filter(medicine_uid = input.medicine).first()
        dosage = Dosage.objects.create(
            medicine =medicine,
            amount = input.amount,
            frequency = input.frequency
        )
        data = PatientBuilder.resolve_get_dosage(id = dosage.dose_uid)
        print(" what is this :", dosage.dose_uid )
        print(" this is the data :", data)
        return self(response = ResponseObject.get_response(id = '6'), data = data)

class CreateMedicinePrescriptionMutation(graphene.Mutation):
    class Arguments:
        input = MedicinePrescritpionInputObject(required= True)
    response = graphene.Field(ResponseObject)
    data = graphene.Field(MedicinePrescriptionObject)
    
    @classmethod
    def mutate(self, root, info, input):
        medicine = MedicineInformation.objects.filter(medicine_uid = input.medicine).first()
        dosage = Dosage.objects.get(dose_uid = input.dosage).first()
        prescription = MedicinePrescription.objects.create(
            prescription_name = input.prescription_name,
            dosage = dosage,
            medicine = medicine
        )
        
        data = PatientBuilder.resolve_get_prescritpion(id = prescription.prescriptionID)
        return self(response = ResponseObject.get_response(id = '6'), data = data)
    
class Mutation(graphene.ObjectType):
    create_patient_records_mutation = CreatePatientRecordsMutation.Field()
    create_medicine_mutation = CreateMedicineMutation.Field()
    create_dosage_mutation = CreateDosageMutation.Field()
    create_medicine_prescription_mutation = CreateMedicinePrescriptionMutation.Field()
    
    
    update_patient_records_mutation = UpdatePatientRecordsMutation.Field()

schema = graphene.Schema(mutation=Mutation)