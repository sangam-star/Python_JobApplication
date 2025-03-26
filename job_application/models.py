from django.db import models

# Create your models here.
 
class JobApplication(models.Model):
    job_title = models.CharField(max_length=100)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    application_date = models.DateTimeField(auto_now_add=True)
##

# job_application/models.py
from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



##
    def __str__(self):
        return f'{self.applicant_name} - {self.job_title}'



 