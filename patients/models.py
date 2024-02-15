import uuid
from django.db import models

# Create your models here.

MEDICINE_CHOICES = (
    ('LIQUID', 'LIQUID'),
    ('TABLET', 'TABLET'),
    ('CAPSULES', 'CAPSULES')
)
class MedicineInformation(models.Model):
    medicine_uid = models.UUIDField(editable =False, default = uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.CharField(max_length=100)
    medicine_type = models.CharField(max_length=100, default='', choices=MEDICINE_CHOICES, blank = True)
    medicine_created_date = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
        return self.name
    
class Dosage(models.Model):
    dose_uid = models.UUIDField(editable = False, default= uuid.uuid4)
    medicine = models.ForeignKey(MedicineInformation, on_delete= models.PROTECT)
    amount = models.CharField(max_length=50)
    frequency = models.CharField(max_length =50)
    dose_created_date = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.amount
    
    class Meta:
        ordering = ['-dose_created_date']
    
class MedicinePrescription(models.Model):
    prescriptionID = models.UUIDField(primary_key = True, editable=False, default= uuid.uuid4)
    prescription_name = models.CharField(max_length=100)
    dosage = models.ForeignKey(Dosage, on_delete= models.PROTECT)
    medicine = models.ForeignKey(MedicineInformation, on_delete = models.CASCADE)
    prescription_created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.prescription_name
    
    class Meta:
        ordering = ['-prescription_created_date']
    

class PatientRecords(models.Model):
    patientID = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    medication = models.ForeignKey(MedicineInformation, on_delete=models.PROTECT, blank = True, null=True)
    dosage = models.ForeignKey(Dosage, on_delete=models.PROTECT, blank = True, null = True)
    prescrition = models.ForeignKey(MedicinePrescription, on_delete= models.PROTECT, null = True, blank = True, default = '')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits = 10, decimal_places = 2)
    patient_created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering =['-patient_created_date']



    

        
